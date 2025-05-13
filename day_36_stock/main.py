import os
from dotenv import load_dotenv
import requests
from datetime import datetime, timedelta 
from news import get_news

news_text = get_news()
load_dotenv()

stock_end_point = "https://www.alphavantage.co/query"

stock_parameters = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : "BTCUSD",
    "apikey" : os.getenv("stock_api_key")
}

stock_response = requests.get(
    stock_end_point,
    params=stock_parameters
)

stock_response.raise_for_status()
stock_data = stock_response.json()


today = datetime.now().date() #Get today's date

yesterday = str(today - timedelta(days=1))
day_before_yesterday = str(today - timedelta(days=2))

yesterday_price = (stock_data["Time Series (Daily)"][yesterday]["4. close"]) #price close for  yesterday
day_before_yesterday_price = (stock_data["Time Series (Daily)"][day_before_yesterday]["4. close"]) #price close for day before yesterday
print(yesterday_price, day_before_yesterday_price)

# check if there is  🔺5% or 🔻5%

# yesterday_price = 100
# day_before_yesterday_price = 110

price_change = (float(yesterday_price) / float(day_before_yesterday_price))
percent_change = (price_change - 1) * 100
rounded_percent_change = round(percent_change, 0) #float

if abs(rounded_percent_change) > 5:
    print(f"{stock_parameters['symbol']} change is {rounded_percent_change}% \n\n{news_text}")