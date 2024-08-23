from flask import render_template
from app import app


@app.route('/')  #decorator
@app.route('/index')


def index():
    user = {'username': 'Gaia'}

    posts = [{'author': {'username': 'Gaia'},
              'body': 'Beautiful day in Portland!'},

             {'author': {'username': 'Amadeus'},
              'body': 'The Avengers movie was so cool'}]

    return render_template('index.html', title='Home', user=user, posts=posts)







