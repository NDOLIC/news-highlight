from app import app
import urllib.request,json
from .models import sources

sources = sources.sources

# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the movie base url
base_url = app.config["NEWS_API_BASE_URL"]


# def get_sources(category):
#     '''
#     Function that gets the json response to our url request
#     '''
#    

#     with urllib.request.urlopen(get_sources_url) as url:
#         get_sources_data = url.read()
#         get_sources_response = json.loads(get_sources_data)

#         sources_sources = None

#         if get_sources_response['sources']:
#             sources_sources_list = get_sources_response['sources']
#             sources_sources = process_sources(sources_sources_list)


#     return sources_sources
def get_sources(category):
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = base_url.format(category,api_key)
    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response= json.loads(get_sources_data)

        sources_results = None
        if get_sources_response['sources']:
            sources_list = get_sources_response['sources']
            sources = process_sources(sources_list)
    return sources_results

def process_sources(sources_list):
    '''
    Function that processes the news sources and transform them to a list of Objects
    Args:
        sources_list: A list of dictionaries that contain news details
    Returns :
        news_sources: A list of sources objects
    '''
    news_sources = []
    for news_source in sources_list:
        source_id = news_source.get('id')
        source_name = news_source.get('name')
        source_url= news_source.get('url')
        source_description=news_source.get('description')
        source_category= news_source.get('category')
        source_language=news_source.get('language')

        news_source = NewsSource(source_id,source_name,source_description,source_url,source_category,source_language)
        news_sources.append(news_source)

    return news_sources
