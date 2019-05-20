import os
import pandas as pd
import json
import datetime as dt
from datetime import datetime, date
from time import sleep
from kafka import KafkaProducer


KEY_METRICS_TOPIC = os.environ.get('KEY_METRICS_TOPIC')
KAFKA_BROKER_URL = os.environ.get('KAFKA_BROKER_URL')
TRANSACTIONS_PER_SECOND = float(os.environ.get('TRANSACTIONS_PER_SECOND'))
SLEEP_TIME = 1 / TRANSACTIONS_PER_SECOND


def get_km_event() -> dict:

    # Import key_metrics.json file:
    km_df = pd.read_json('key_metrics.json', orient='columns')

    # list of dicts for report column - data row
    km_rd = km_df['report']['data']

    # list of dicts for report column - metrics row:
    km_rm = km_df['report']['metrics']

    # Create a list of the metric names:
    metric_names = [mt_dict['name'].lower().replace(" ", "_") for mt_dict in km_rm]

    for rd in km_rd:
        dt_metric_dict = {}
        # Counts per date:
        counts = [float(count) if count.upper() != 'INF' else 0 for count in rd['counts']]
        # Zip togther metic names with counts list:
        metric_dict = dict(zip(metric_names, counts))
        #print(metrics)
        # convert to datetime:
        date_str = str(rd['year']) + ' ' +  str(rd['month']) + ' ' + str(rd['day'])
        dt_date = dt.datetime.strptime(date_str, '%Y %m %d').date()
        #print(dt_date)
        dt_metric_dict['date'] = dt_date
        dt_metric_dict.update(metric_dict)
        yield dt_metric_dict


if __name__ == '__main__':

    t1_producer = KafkaProducer(
        bootstrap_servers=KAFKA_BROKER_URL,
        # Encode all values as JSON
        value_serializer=lambda value: json.dumps(value, default=str).encode(),
    )

    km_gen = get_km_event()

    _empty = object()

    while True:
        try:
            km_event: dict = next(km_gen)
        except StopIteration:
            print('The generator is empty')
            km_event = _empty
            break

        if km_event != _empty:
            t1_producer.send(KEY_METRICS_TOPIC, value=km_event)
            print(km_event)  # DEBUG
