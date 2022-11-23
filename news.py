import requests
import sys

url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=ab42f6e37d7b447bacdaf4018551d51a"

news = requests.get(url)

if news.status_code != 200:
    sys.exit("Bad Request")

news=news.json()
articles = news["articles"]

article_titles = []
article_descriptions = []
article_authors = []
article_url = []

for article in articles:
	Title = article['title']
	desc = article['description']
	auth = article['author']
	url = article['url']
	print('Title: %s' % Title)
	print('Description: %s' % desc)
	print('Author: %s'% auth)
	print('Link: %s' % url)
	print('\n')
