from app import app
import urllib.request,json
from .models import news

# Getting api key
api_key = app.config['NEWS_API_KEY']

News = news.News


# Getting the movie base url
base_url = app.config["NEWS_API_BASE_URL"]