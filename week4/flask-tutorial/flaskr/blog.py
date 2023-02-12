from flask import render_template, request, redirect, url_for
# render_template is used to render templates (HTML files) with variables.
# request is used to access information about the incoming request.
# redirect is used to redirect the user to a different URL.
# url_for is used to generate URLs for view functions.

from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db
# Blueprint is used to define a blueprint, a way to organize a group of related views and other code.
# flash is used to display a message to the user.
# g is a special object that is unique for each request. It is used to store data that might be accessed by multiple functions during the request.
# abort is used to return an HTTP error response.
# login_required is a decorator that can be used to make a view require authentication.
# get_db is a function that returns a database connection

bp = Blueprint('blog', __name__)

@bp.route('/')
def index():
# a view function that returns the blog index page, showing a list of posts with the most recent post first. The view queries the database for the posts and passes the resulting list of posts to the template.
    db = get_db()
    posts = db.execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()
    return render_template('blog/index.html', posts=posts)

@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
# a view function that allows the user to create a new post. If the request method is POST, the view reads the data from the form, validates it, and if the data is valid, inserts a new post into the database. If the request method is GET, the view returns the create post form.
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO post (title, body, author_id)'
                ' VALUES (?, ?, ?)',
                (title, body, g.user['id'])
            )
            db.commit()
            return redirect(url_for('blog.index'))

    return render_template('blog/create.html')

def get_post(id, check_author=True):
# a helper function that gets a post from the database by its ID and verifies that the post exists and, if check_author is True, that the current user is the author of the post. If either of these checks fail, the function raises an error.
    post = get_db().execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' WHERE p.id = ?',
        (id, )
    ).fetchone()

    #print("Got the post, but...")

    if post is None:
        abort(404, f"Post id {id} doesn't exist.")

    if check_author and post['author_id'] != g.user['id']:
        abort(403)

    return post

# hy204: OCP, The check_author argument is defined so that the function can be used to get a post without checking the author. It is open to use with checking.

@bp.route('/<int:id>/update', methods=('GET', 'POST'))# where is GET used?
@login_required
def update(id):
# a view function that allows the user to update an existing post. If the request method is POST, the view reads the data from the form, validates it, and if the data is valid, updates the post in the database. If the request method is GET, the view returns the update post form pre-populated with the post data.
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'UPDATE post SET title = ?, body = ?'
                ' WHERE id = ?',
                (title, body, id)
            )
            db.commit()
            return redirect(url_for('blog.index'))

    return render_template('blog/update.html', post=post)

@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
# a view function that allows the user to delete a post. If the request method is POST, the view deletes the post from the database.
    get_post(id)
    db = get_db()
    db.execute('DELETE FROM post WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('blog.index'))

@bp.route('/<int:id>/harmless_browse')
def detail(id):# detail(id)
    # print('post_id:', id)
    post = get_post(id, check_author=False)
    # print('post:', post)
    return render_template('blog/post_detail.html', post=post)

