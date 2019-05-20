import psycopg2

conn = psycopg2.connect(
    host='localhost',
    port=5432,
    dbname='dss_db_dev',
    user='postgres',
    password='postgres'
)
cur = conn.cursor()
cur.execute("SELECT * FROM task1_km;")
result = cur.fetchall()
print(result)
conn.commit()
cur.close()
conn.close()
