
from flask import render_template
from app import app



# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    title = 'Home - Welcome to The best News Review Website Online'
    return render_template('index.html', title = title)


@app.route('/new/<new_id>')
def movie(new_id):

    '''
    View new page function that returns the new details page and its data
    '''
    title = f'You are viewing {new_id}'
    return render_template('new.html',title = title)