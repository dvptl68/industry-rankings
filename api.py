# Groups companies by industry and ranks top companies by stock performance
import requests
import json

# API key for Alpha Vantage
apiKey = ''
with open('key.txt') as f:
  apiKey = f.read()

# API call to Alpha Vantage
ticker = input('Enter a company stock abbreviation: ')
url = f'https://www.alphavantage.co/query?function=NEWS_SENTIMENT&tickers={ticker}&topics=technology&limit=50&apikey={apiKey}'
r = requests.get(url)
data = r.json()

# Prints the data to a file
with open('out.json', 'w+') as f:
  f.write(json.dumps(data, indent=4))

total_sentiment = 0
for news in data["feed"]:
  score = news["ticker_sentiment"][0]["ticker_sentiment_score"]
  total_sentiment += float(score)

print(f"Overall sentiment score of {ticker}: {total_sentiment}")
