from flask import Flask, render_template, request, redirect, url_for
import requests

from config import NEWS_API_KEY

# Create the Flask app
app = Flask(__name__)