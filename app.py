from flask import Flask, render_template, request, redirect, url_for
import requests
from dotenv import load_dotenv
import os


# from config import NEWS_API_KEY

# Load environment variables from .env file
load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")

# Create the Flask app
app = Flask(__name__)

# Define the home page route
@app.route('/')
def home():
    try:
        query = request.args.get("query", "latest")
        url = f"https://newsapi.org/v2/everything?q={query}&apiKey={NEWS_API_KEY}"
        response = requests.get(url)
        data = response.json()
        articles = data["articles"]
        filtered_articles = [article for article in articles if "Yahoo" not in article["source"]["name"] and 'removed' not in article["title"].lower()]
        return render_template("index.html", articles=filtered_articles)
    except:
        return render_template("404.html")

if __name__ == "__main__":
    app.run(debug=True)