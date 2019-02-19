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
    technology_sources = get_sources('technology')
    sciences_sources = get_sources('science')
    entertainment_sources = get_sources('entertainment')
    health_sources = get_sources('health')

    title = 'Home-Welcome to the Breaking news updates'
    return render_template('index.html', title = title,general = general_sources, business= business_sources,sports=sports_sources,technology=technology_sources,science=sciences_sources,entertainment=entertainment_sources,health=health_sources)
