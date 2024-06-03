from flask import Flask,  url_for

app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page'


@app.route('/login')
def login():
    return '''
<!DOCTYPE html>
<html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="{}">
        <title>static file in Flask</title>
    </head>

    <body>
     <p>Welcome to Login page </p>

    </body>

</html>
'''.format(url_for('static', filename='style.css'))


""" 
Static Files
-------------

Dynamic web applications also need static files. 

That's usually where the CSS and JavaScript files 
are coming from. 

Ideally your web server is configured to serve them 
for you, but during development Flask can do that as 
well. 

Just create a folder called static in your package 
or next to your module and it will be available at 
/static on the application.

To generate URLs for static files, use the special 
'static' endpoint name

The file has to be stored on the filesystem as 
static/style.css.

"""
