import requests
import json

from model.news import News

def update_feed(country):
    response = requests.get('https://newsapi.org/v2/top-headlines?country={}&apiKey=9869a9ba9eb44cdfbbc13e1a91637860'.format(country))

    try:
        f = open('cache/news.txt', 'w+')
        f.write(json.dumps(response.json()))
        f.close()
    except Exception as ex:
        print str(ex)
        return False
    
    return True


def search(author, source):
    news = []
    try:
        f = open('cache/news.txt', 'r')
        data = json.loads(f.read())
        f.close()
        articles = data['articles']
        for article in articles:
            if author is not None:
                if article['author'] is not None:
                    if author in article['author']:
                        news.append(News.news_from_dict(article))
            elif source is not None:
                if 'source' in article and \
                    'name' in articles['source'] and \
                    article['source']['name'] is not None:
                    if source in article['source']['name']:
                        news.append(News.news_from_dict(article))
        
    except Exception as ex:
        print str(ex)

    return news

    