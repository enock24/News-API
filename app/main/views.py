from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_news,get_news,search_news
from .forms import ReviewForm
from ..models import Review

Review=Review



# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular movie
    popular_news = get_news('popular')
    upcoming_news = get_news('upcoming')
    now_showing_news= get_news('now_playing')

    title = 'Home - Welcome to The best News Review Website Online'

    search_news = request.args.get('news_query')

    if search_news:
        return redirect(url_for('.search',news_name=search_news))
    else:
        return render_template('index.html', title = title, popular = popular_news, upcoming = upcoming_news, now_showing = now_showing_news )


@main.route('/movie/<int:id>')
def news(id):

    '''
    View news page function that returns the news details page and its data
    '''
    news = get_news(id)
    title = f'{news.title}'
    reviews = Review.get_reviews(news.id)

    return render_template('news.html',title = title,movie = news,reviews = reviews)



@main.route('/search/<news_name>')
def search(news_name):
    '''
    View function to display the search results
    '''
    news_name_list = news_name.split(" ")
    news_name_format = "+".join(news_name_list)
    searched_news = search_news(news_name_format)
    title = f'search results for {news_name}'
    return render_template('search.html',movies = searched_news)


@main.route('/news/review/new/<int:id>', methods = ['GET','POST'])
def new_review(id):

    form = ReviewForm()

    news = get_news(id)

    if form.validate_on_submit():
        title = form.title.data
        review = form.review.data

        new_review = Review(news.id,title,news.poster,review)
        new_review.save_review()

        return redirect(url_for('.news',id = news.id ))

    title = f'{news.title} review'
    return render_template('new_review.html',title = title, review_form=form, movie=news)