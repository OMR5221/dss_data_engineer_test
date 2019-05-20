import pandas as pd
import json
import datetime as dt
from datetime import datetime, date
import psycopg2


# Import key_metrics.json file:
km_df = pd.read_json('key_metrics.json', orient='columns')

# list of dicts for report column - data row
km_rd = km_df['report']['data']

# list of dicts for report column - metrics row:
km_rm = km_df['report']['metrics']

# Create a list of the metric names:
metric_names = [mt_dict['name'].lower().replace(" ", "_") for mt_dict in km_rm]

key_metrics_data = []

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
    # print(dt_metric_dict)
    key_metrics_data.append(dt_metric_dict)

print(key_metrics_data)

# Write data out to file:
with open('task1_key_metrics.json', 'w') as f:
    f.write(json.dumps(key_metrics_data, default=str))
