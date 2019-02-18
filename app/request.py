from app import app
import urllib.request,json
from .models import sources

sources = sources.sources

# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the movie base url
base_url = app.config["NEWS_API_BASE_URL"]


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
            sources_sources_list = get_sourcess_response['sources']
            sources_sources = process_sources(sources_sources_list)


    return sources_sources