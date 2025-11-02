import pandas as pd
import requests
import os
from dotenv import load_dotenv

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID =os.getenv("CHAT_ID")




load_dotenv()

def post_to_twitter(headline, summary, link):
    pass  # not implemented yet

def post_to_telegram(headline, summary, link):
   
    message = f"📰 {headline}\n\n{summary}\nRead more: {link}"

    print("Sending message:")
    print(message)
    
    response = requests.get(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        params={"chat_id": CHAT_ID, "text": message}
    )
    print(response.json())

def get_today_news():
    return pd.read_csv("categorized_summary_upadated_data.csv")

def main():
    news_items = get_today_news()
    print("News length:", len(news_items))

    for _, item in news_items.head(3).iterrows():
        post_to_telegram(item['title'], item['summary'], item['link'])


if __name__ =="__main__":
    main()
