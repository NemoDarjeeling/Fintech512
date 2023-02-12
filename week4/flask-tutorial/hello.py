from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!<br>Get through'flask --app hello run'"
