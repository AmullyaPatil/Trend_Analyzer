# Backend: FastAPI Boilerplate

from fastapi import FastAPI
from pymongo import MongoClient
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import requests

app = FastAPI()
client = MongoClient("mongodb://localhost:27017/")
db = client["TrendAnalyzer"]
analyzer = SentimentIntensityAnalyzer()

# Fetch and Store Trends
@app.get("/fetch-trends/{category}")
def fetch_trends(category: str):
    if category == "news":
        response = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=YOUR_API_KEY")
        data = response.json()
        for article in data["articles"]:
            sentiment = analyzer.polarity_scores(article["title"])  # Sentiment Analysis
            trend = {"category": category, "title": article["title"], "sentiment": sentiment}
            db.trends.insert_one(trend)
    return {"message": "Trends fetched and stored"}

# Get Stored Trends
@app.get("/trends/{category}")
def get_trends(category: str):
    trends = list(db.trends.find({"category": category}, {"_id": 0}))
    return {"trends": trends}
