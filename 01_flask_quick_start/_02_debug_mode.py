from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello World of Flask !</p>"

# flask --app file_name run --debug


"""
The `flask run` command can do more than just start 
the development server. 

By enabling debug mode, the server will automatically 
reload if code changes, and will show an interactive 
debugger in the browser if an error occurs during a 
request.


Warning
--------
The debugger allows executing arbitrary Python code 
from the browser. It is protected by a pin, but still 
represents a major security risk. 

--> Do not run the development server or debugger in 
    a production environment.

"""
