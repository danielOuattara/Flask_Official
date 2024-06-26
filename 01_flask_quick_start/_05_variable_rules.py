from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello World of Flask !</p>"


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'


@app.route('/product/<uuid:productId>')
def show_product(productId):
    # show the productId
    return f'productId: {escape(productId)}'


"""

Variable Rules
---------------
You can add dynamic sections to a URL by marking 
sections with <variable_name> in @route() 

Your function then receives the <variable_name> as 
a keyword argument. 

Optionally, you can use a converter to specify the 
type of the argument like <converter:variable_name>.

Converter types:
-----------------
string: (default) accepts any text without a slash
int: accepts positive integers
float: accepts positive floating point values
path: like string but also accepts slashes
uuid: accepts UUID strings

"""
