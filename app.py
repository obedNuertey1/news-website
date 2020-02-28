from flask import Flask, render_template, request, redirect, url_for
import requests

from config import NEWS_API_KEY

# Create the Flask app
app = Flask(__name__)

# Define the home page route
@app.route('/')
def home():
    query = request.args.get("query", "latest")
    url = f"https://newsapi.org/v2/everything?q={query}&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    data = response.json()
    
if __name__ == "__main__":
    app.run(debug=True)