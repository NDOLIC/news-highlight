from app import app
import urllib.request,json
from .models import sources
from .models import articles

Sources = sources.Sources
Articles=articles.Articles

# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the movie base url
base_url = app.config["NEWS_API_BASE_URL"]
article_url=app.config["ARTICLE_API_BASE_URL"]


def get_sources(category):
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_sources = None

        if get_sources_response['sources']:
            sources_sources_list =get_sources_response['sources']
            sources_sources = process_sources(sources_sources_list)


    return sources_sources


def process_sources(sources_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects

    Args:
        sources_list: A list of dictionaries that contain movie details

    Returns :
        sources_results: A list of movie objects
    '''
    sources_sources = []
    for sources_item in sources_list:
        id = sources_item.get('id')
        name = sources_item.get('name')
        description = sources_item.get('description')
        url = sources_item.get('url')
        category = sources_item.get('category')
        language = sources_item.get('language')

        if category:
            news_object = Sources(id,name,description,url,category,language)
            sources_sources.append(news_object)

    return sources_sources



def get_articles(source_id):
    '''
    Function that gets the json response to our url request for a specific source
    '''
    get_articles_url = article_url.format(source_id, api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['articles']:
            articles_list = get_articles_response['articles']
            articles_results = process_articles_results(articles_list)

    return articles_results


def process_articles_results(articles_list):
    '''
    Function  that processes the article result and transform them to a list of Objects
    Args:
        articles_list: A list of dictionaries that contain article details
    Returns :
        articles_results: A list of source objects
    '''
    article_results = []

    for article in articles_list:
        id = article.get('id')
        name = article.get('name')
        author = article.get('author')
        title = article.get('title')
        description = article.get('description')
        url = article.get('url')
        image = article.get('urlToImage')
        publishedAt = article.get('publishedAt')

        article_object = Articles(id,name,author, title, description, url, image, publishedAt)
        article_results.append(article_object)

    return article_results
