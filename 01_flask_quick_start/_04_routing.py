from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def index():
    return " Index page"


# @app.route('/hello')
# def hello():
#     return 'Hello world of Flask !'


@app.route("/<name>")
def hello_user(name):
    if name == 'hello':
        return 'Hello world of Flask !'
    else:
        return f"Hello, {escape(name)}!"


"""
Routing
--------
Modern web applications use meaningful URLs to help users. 
Users are more likely to like a page and come back if the 
page uses a meaningful URL they can remember and use to 
directly visit a page.

Use the `route()` decorator to bind a function to a URL.
"""
