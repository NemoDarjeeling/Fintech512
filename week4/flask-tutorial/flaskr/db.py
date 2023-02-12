import sqlite3
#imports the sqlite3 module, which provides a way to interact with SQLite databases in Python.
import click
#imports the click module, which is a library for building command line interfaces in Python.
from flask import current_app, g
# imports the current_app and g objects from the flask module. current_app is a proxy object for the current Flask application and g is a global object that is unique for each request and can store data that might be accessed by multiple functions during the request.
def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db
#a function that creates a new connection to the SQLite database if one does not already exist for the current request and stores it in the g object. If the connection already exists, it returns the existing connection. The connection information is taken from the DATABASE configuration key in the current Flask application.

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()
#a function that closes the SQLite database connection and removes it from the g object. The e argument is an optional error that might be passed to the function and is not used in this case.

# hy204: SRP, get_db function connects to a database if it doen't exist(one responsibility), close_db function is only responsible for close db

def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))
#a function that initializes the database by executing a SQL script located at schema.sql. It calls the get_db function to get a connection to the database and then uses the executescript method to execute the script.

@click.command('init-db')
#a decorator that defines a new CLI command called init-db. When this command is executed, it calls the init_db_command function.
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
#a function that takes a Flask application as its argument and sets it up to use the database functions defined in this module. It registers the close_db function as a function that should be called when the application context is torn down using the teardown_appcontext method. It also adds the init_db_command function as a CLI command using the add_command method of the cli object.
