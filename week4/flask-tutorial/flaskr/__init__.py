import os

from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return "Hello, World!"

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    return app

# import os: This line imports the os module, which provides a way to interact with the operating system, including access to the file system.
# from flask import Flask: This line imports the Flask class from the Flask library. The Flask class is the base for creating Flask applications.
# def create_app(test_config=None):: This line defines the function create_app, which takes an optional argument test_config that is used to load a test configuration. If test_config is not provided, the function will use a default configuration.
# app = Flask(__name__, instance_relative_config=True): This line creates an instance of the Flask class, passing __name__ as the first argument and instance_relative_config=True as the second argument. __name__ refers to the name of the module, which is useful for finding resources relative to the module. instance_relative_config specifies that configuration files should be relative to the instance folder.
# app.config.from_mapping(SECRET_KEY='dev', DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite')): This line uses the from_mapping method to set the SECRET_KEY and DATABASE configuration variables. The SECRET_KEY is set to 'dev', which is a placeholder value used during development. The DATABASE is set to the path of a SQLite database file named 'flaskr.sqlite' that is located in the instance folder.
# if test_config is None:: This line checks if the test_config argument was provided.
# app.config.from_pyfile('config.py', silent=True): This line uses the from_pyfile method to load the configuration from a file named 'config.py' that is located in the instance folder. The silent argument is set to True, which means that if the file does not exist, an error will not be raised.
# else:: This line is executed if the test_config argument was provided.
# app.config.from_mapping(test_config): This line uses the from_mapping method to load the configuration from the test_config argument.
# try:: This line tries to create the instance folder using the makedirs method from the os module.
# os.makedirs(app.instance_path): This line creates the instance folder using the makedirs method.
# except OSError:: This line catches an OSError that is raised if the instance folder already exists.
# @app.route('/hello'): This line is a decorator that creates a route for the hello function. The route maps to the URL path /hello.
# def hello():: This line defines the hello function that returns a string "Hello, World!" when called.
# from . import db: This line imports the db module from the current package.

# hy204: SRP, the whole function here creates a new app along with basic configurations, which is necessary for creating an App
# hy204: OCP, the default is set as test_config=None, however, this function is open for different configurations