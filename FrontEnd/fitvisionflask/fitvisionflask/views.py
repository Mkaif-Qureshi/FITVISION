from datetime import datetime
from flask import render_template, request
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
    # Dummy session request entries
    session_request1 = {
        "user_name": "User 1",
        "user_email": "user1@example.com",
        "user_phone": "123-456-7890",
        "session_type": "Personal Training",
        "preferred_trainer": "Trainer A",
        "session_date": "2024-03-10",
        "session_time": "10:00 AM",
    }

    session_request2 = {
        "user_name": "User 2",
        "user_email": "user2@example.com",
        "user_phone": "987-654-3210",
        "session_type": "Group Training",
        "preferred_trainer": "Trainer B",
        "session_date": "2024-03-12",
        "session_time": "02:00 PM",
    }

    # Create a list of session requests
    session_requests_data = [session_request1, session_request2]

    return render_template('session_requests.html', session_requests=session_requests_data)



# @app.route('/book_session', methods=['GET', 'POST'])
# def book_session():
#     if request.method == 'POST':
#         full_name = request.form.get('fullName')
#         email = request.form.get('email')
#         phone = request.form.get('phone')
#         session_type = request.form.get('sessionType')
#         preferred_trainer = request.form.get('preferredTrainer')
#         session_date = request.form.get('sessionDate')
#         # Add your session booking logic here


#     return render_template('book_session.html')


from flask import render_template
from flask.views import MethodView

class CameraView(MethodView):
    def get(self):
        return render_template('camera.html')

# Add the route for the CameraView
app.add_url_rule('/camera', view_func=CameraView.as_view('camera'))