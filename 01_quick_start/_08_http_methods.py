from flask import Flask, request

app = Flask(__name__)


def do_the_login():
    return 'do login'


def show_the_login_form():
    return 'show form'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()


"""
HTTP Methods
-------------

Web applications use different HTTP methods when accessing URLs. 
You should familiarize yourself with the HTTP methods as you work 
with Flask. 

By default, a route only answers to GET requests. 

You can use the methods argument of the `route()` decorator to 
handle different HTTP methods.

The example above keeps all methods for the route within one function, 
which can be useful if each part uses some common data.

You can also separate views for different methods into different 
functions. Flask provides a shortcut for decorating such routes 
with `get()`, `post()`, etc. for each common HTTP method.
"""


@app.get('/login')
def login_get():
    return show_the_login_form()


@app.post('/post')
def login_post():
    return do_the_login()


@app.put('/post')
def update_post():
    return "Updating the data"


@app.delete('/post')
def delete_post():
    return "Deleting the data"


"""
If GET is present, Flask automatically adds support for 
the HEAD method and handles HEAD requests according to 
the HTTP RFC. 

Likewise, OPTIONS is automatically implemented for you.
"""
