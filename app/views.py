from flask import render_template
from flask import request
from app import app
from .request import get_sources


@main.route('/')

def index():

    '''
    This view function returns the index page and its data
    '''

    news_sources=get_sources()
    title = 'Home-Welcome to the Breaking news updates'
    return render_template('index.html',title=title, sources=news_sources)


