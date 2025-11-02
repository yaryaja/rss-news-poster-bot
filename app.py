import streamlit as st
import pandas as pd



# static html website
# html = df.to_html(index=False, escape=False)
# with open("tech_news.html", "w", encoding="utf-8") as f:
#     f.write("<h1>Tech News Summary</h1>")
#     f.write(html)

st.set_page_config(page_title="Tech News Dashboard", layout="wide")

df = pd.read_csv("categorized_summary_upadated_data.csv")
# df = df.sort_values(by="published", ascending=False)


st.title("📰 Tech News Dashboard")
st.write("Auto-collected, summarized, and categorized news feeds")

category = st.multiselect("Filter by category", df["category"].unique())
if category:
    df = df[df["category"].isin(category)]

search = st.text_input("Search by keyword")
if search:
    df = df[df["title"].str.contains(search, case=False, na=False)]

st.dataframe(df[["title", "short_summary", "category", "link"]])
