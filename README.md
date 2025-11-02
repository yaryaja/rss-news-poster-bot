# 📰 News Automation Bot

An automated system that collects the latest technology news from multiple RSS feeds, removes duplicates, summarizes articles using AI, and automatically posts the top stories to Telegram (and optionally Twitter).

---

## 🚀 Features

- 🧠 **RSS Feed Parsing:** Collects articles from multiple tech news sources (e.g., TechCrunch, The Verge, etc.)  
- 🔍 **Deduplication:** Removes repeated or similar news items from different feeds  
- ✂️ **AI Summarization & Categorization:** Generates concise summaries and classifies news (Tech, Business, Science, etc.)  
- 🤖 **Automated Posting:** Posts summarized news automatically to a Telegram channel or chat  
- ⏰ **Daily Scheduling (optional):** Use GitHub Actions or cron job to run the bot automatically every day  

---


## 🏗️ Project Structure

```
news_automation/
├── main.py # Step 1: Parse RSS feeds and deduplicate
├── summarize.py # Step 2: Summarize into short summary
├── classification.py # Step 3: Classified news 
├── vizualize.py # Step 3: Display/export data
├── automation.py # Step 4: Automate tasks(yet to be implemented)
├── poster.py # Step 5: Post to Telegram or Twitter
│
├── categorized_summary_updated_data.csv # Output of summarized data
├── requirements.txt
└── README.md

```
---

## ⚙️ Installation

### 1️⃣ Clone this repository
```bash
git clone https://github.com/<your-username>/news_automation.git
cd news_automation

```
###  Install dependencies
```bash
pip install -r requirements.txt
```

## Create a .env file or define environment variables:
```bash
BOT_TOKEN=your_telegram_bot_token
CHAT_ID=your_chat_id
OPENAI_API_KEY=your_gemini_api_key   # if using AI summarization
```





## Future Enhancements

🏷️ Add trending-topic analysis

💬 Include sentiment detection (positive/negative/neutral)

📬 Email or Discord notifications

🌐 Host a live Streamlit dashboard
