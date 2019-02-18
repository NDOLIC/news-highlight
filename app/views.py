from flask import render_template
from flask import request
from app import app
from .request import get_sources


@app.route('/')

def index():

    '''
    This view function returns the index page and its data
    '''
todays_highlights = get_news("general")
    todays_weather = get_news('weather')
    todays_sports = get_news('sports')
    news_sources = get_sources('sources')
    title = 'Home-Welcome to the Breaking news updates'
    return render_template('index.html', title=title, general=todays_highlights ,weather=todays_weather,sports=todays_sports)
    
    # return render_template('index.html',title=title, sources=news_sources)


