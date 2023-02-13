import functools
#imports the functools module, which is used to modify the behavior of functions in the code.
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

# Blueprint is used to define a blueprint for the authentication functionality in the web application.
# flash is used to send a message to the next request, which can be used for error or informational messages.
# g is a global object that can be used to store data during a request-response cycle.
# redirect is used to redirect the user to a different URL.
# render_template is used to render a Jinja2 template and return the result to the user.
# request is an object that represents the current request and can be used to access data from the request.
# session is used to store data that is specific to a user session.
# url_for is used to build URLs for the application's views.
from werkzeug.security import check_password_hash, generate_password_hash
# check_password_hash is used to verify that a password matches the stored password hash.
# generate_password_hash is used to generate a password hash that can be stored in the database.
from flaskr.db import get_db
# imports the get_db function from the flaskr.db module, which returns a database connection.
bp = Blueprint('auth', __name__, url_prefix='/auth')
# creates a blueprint called auth with a URL prefix of /auth.
@bp.route('/register', methods=('GET', 'POST'))
def register():
# If the request method is POST, it retrieves the username and password from the request form data, and inserts the new user into the database if the username and password are provided and the username is not already registered.
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'

        if error is None:
            try:
                db.execute(
                    "INSERT INTO user (username, password) VALUES (?, ?)",
                    (username, generate_password_hash(password)),
                )
                db.commit()
            except db.IntegrityError:
                error = f"User {username} is already registered."
            else:
                return redirect(url_for("auth.login"))

        flash(error)

    return render_template('auth/register.html')

@bp.route('/login', methods=('GET', 'POST'))
def login():
# If the request method is POST, it retrieves the username and password from the request form data, and verifies that the provided username and password match a user in the database.
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))

        flash(error)

    return render_template('auth/login.html')

@bp.before_app_request
# registers a function that runs before the view function, no matter what URL is requested. 
def load_logged_in_user():
# It retrieves the user ID from the session, and sets the g.user variable to the corresponding user from the database if the user is logged in.
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()

@bp.route('/logout')
def logout():
# It clears the user's session data, effectively logging the user out.
    session.clear()
    return redirect(url_for('index'))

def login_required(view):
# view: A view is a representation of an entire system from the perspective of a related set of concerns. It is used to describe the system from the viewpoint of different stakeholders such as end-users, developers, project managers, and testers.
# It takes a view function as an argument and returns a wrapped version of the view that checks if the user is logged in before executing the view.
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view

# hy204: ISP, separated interfaces intended only for register, login, logout.

