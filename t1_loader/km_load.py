import json
import os
import psycopg2

from kafka import KafkaConsumer, KafkaProducer

KAFKA_BROKER_URL = os.environ.get('KAFKA_BROKER_URL')
KEY_METRICS_TOPIC = os.environ.get('KEY_METRICS_TOPIC')
T1_LOAD_TOPIC = os.environ.get('T1_LOAD_TOPIC')

if __name__ == '__main__':

    t1_loader = KafkaConsumer(
        KEY_METRICS_TOPIC,
        bootstrap_servers=KAFKA_BROKER_URL,
        value_deserializer=lambda value: json.loads(value),
    )
    t1_producer = KafkaProducer(
        bootstrap_servers=KAFKA_BROKER_URL,
        value_serializer=lambda value: json.dumps(value, default=str).encode(),
    )
    counter = 0
    conn = psycopg2.connect(
        host='db',
        port=5432,
        dbname='dss_db_dev',
        user='postgres',
        password='postgres'
    )
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS task1_km (id serial PRIMARY KEY, date TIMESTAMP, page_views INTEGER, visits INTEGER, unique_visitors INTEGER, bounce_rate INTEGER);")

    for key_metric in t1_loader:
        record: dict = key_metric.value
        t1_producer.send(T1_LOAD_TOPIC, value=record)
        cur.execute(
            'INSERT INTO task1_km (date, page_views, visits, unique_visitors, bounce_rate)'
            'VALUES (%(date)s, %(page_views)s, %(visits)s, %(unique_visitors)s, %(bounce_rate)s)',
            record
        )
        conn.commit()

    cur.close()
    conn.close()
