from google import genai

import pandas as pd
import time
api_key="AIzaSyBSSG0CgejElYtLvElR79GFx-jcvNuK_Hc"
client = genai.Client(api_key=api_key)


def summarize_text(text):
    prompt = f"Summarize this tech news in one concise sentence:\n\n{text}"

    response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=[prompt]

    )
    return response.text.strip()



df = pd.read_csv("unique_articles.csv")


summaries=[]
count=0
for i, row in df.iterrows():
    try:
        combined_text = f"{row['title']}\n\n{row['summary']}"
        summaries.append(summarize_text(combined_text))
        time.sleep(0.5)
    except Exception as e:
        summaries.append("")
        print("Error at row", i, ":", e)


df["short_summary"] = summaries

# To save the updated DataFrame back to a CSV file
df.to_csv("short_summary_upadated_data.csv", index=False)






