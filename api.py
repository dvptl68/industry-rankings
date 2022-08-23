# Groups companies by industry and ranks top companies by stock performance

import requests


apiKey = ''
with open('key.txt') as f:
  apiKey = f.read()

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey={apiKey}'
r = requests.get(url)
data = r.json()

print(data)
