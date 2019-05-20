import pandas as pd

data_df = pd.io.json.json_normalize(products_rd)
data_dict = data_df.to_dict(orient='records')

formatted_data = [{'country': country['name'], 'city': city['name'], 'product_name':
product['name'], 'page_views': product['counts'][0], 'visits': product['counts'][1]} for country in
data_dict for city in country['breakdown'] for product in city['breakdown']]

print(formatted_data)
