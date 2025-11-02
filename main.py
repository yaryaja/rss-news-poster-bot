import feedparser
import pandas as pd
from difflib import SequenceMatcher

def is_similar(a, b, threshold=0.85):
    return SequenceMatcher(None, a.lower(), b.lower()).ratio() > threshold


unique_articles=[]
def read_rss_feed(feed_urls):
    """
    Reads and parses an RSS feed from a given URL.

    """
    for feed_url in feed_urls:
        feed = feedparser.parse(feed_url)

        if feed.bozo:  # Check for parsing errors
            print(f"Error parsing feed from {feed_url}: {feed.bozo_exception}")
            return

    
        for entry in feed.entries:
            title = entry.title
            if not any(is_similar(title, a['title']) for a in unique_articles):
                unique_articles.append({
                    "title": title,
                    "link": entry.link,
                    "summary": entry.get("summary", ""),
                    "published":entry.published
                })
         
            

rss_feed_url_1 ="https://techcrunch.com/feed" # Replace with a real RSS feed URL
rss_feed_url_2="https://ir.thomsonreuters.com/rss/news-releases.xml"
rss_feed_urls=[rss_feed_url_1,rss_feed_url_2]
read_rss_feed(rss_feed_urls)

df = pd.DataFrame(unique_articles)
df.to_csv("unique_articles.csv", index=False)
print("Saved", len(df), "articles.")



