def get_news():
    import os
    from dotenv import load_dotenv
    import requests
    from datetime import datetime, timedelta

    load_dotenv()

    today = datetime.now().date()
    yesterday = str(today - timedelta(days=1))

    news_endpoint = "https://newsapi.org/v2/everything"
    news_parameters = {
        "q": "btc",
        "from": yesterday,
        "to": yesterday,
        "apikey": os.getenv("news_api_key")
    }

    news_response = requests.get(
        news_endpoint,
        params=news_parameters
    )

    news_response.raise_for_status()
    news_data = news_response.json()
    news_text = ""

    for i in range(5):
        news_text += news_data["articles"][i]["title"]
        news_text += "\n" * 2

    return news_text