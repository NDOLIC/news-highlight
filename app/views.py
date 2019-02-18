from flask import render_template
from flask import request
from app import app
from .request import get_sources


@app.route('/')

def index():

    '''
    This view function returns the index page and its data
    '''
    
    general_sources = get_sources('general')
    business_sources = get_sources('business')
    sports_sources = get_sources('sports')

    title = 'Home-Welcome to the Breaking news updates'
    return render_template('index.html', title = title,general = general_sources, business= business_sources,sports=sports_sources)
    # return render_template('index.html', title=title, general=todays_highlights ,weather=todays_weather,sports=todays_sports)
    
    # return render_template('index.html',title=title, sources=news_sources)


