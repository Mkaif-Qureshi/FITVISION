from datetime import datetime
from flask import render_template
from fitvisionflask import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/explore')
def explore():
    """Renders the explore page."""
    # Add logic to fetch and display exercises
    return render_template(
        'explore.html',
        title='Explore Exercises',
        year=datetime.now().year,
    )

@app.route('/login')
def login():
    """Renders the login page."""
    return render_template(
        'login.html',
        title='Login',
        year=datetime.now().year,
    )

@app.route('/user_login/book_session')
def book_session():
    """Renders the book session page for users."""
    # Add logic to handle session bookings
    return render_template(
        'book_session.html',
        title='Book a Session',
        year=datetime.now().year,
    )

@app.route('/trainer_login/session_requests')
def session_requests():
    """Renders the session requests page for trainers."""
    # Add logic to handle session requests
    return render_template(
        'session_requests.html',
        title='Session Requests',
        year=datetime.now().year,
    )



