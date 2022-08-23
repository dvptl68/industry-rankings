# Groups companies by industry and ranks top companies by stock performance
import requests
import json

apiKey = ''
with open('key.txt') as f:
  apiKey = f.read()

url = f'https://www.alphavantage.co/query?function=NEWS_SENTIMENT&tickers=AAPL&topics=technology&limit=50&apikey={apiKey}'
r = requests.get(url)
data = r.json()

with open('out.json', 'w+') as f:
  f.write(json.dumps(data, indent=4))
