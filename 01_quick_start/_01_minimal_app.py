from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello World of Flask !</p>"


'''
So what did that code do ? :
    1. First we imported the Flask class. An instance of this class will 
       be our WSGI application.

    2. Next we create an instance of this class. 
       The first argument is the name of the application’s module or package. 
       __name__ is a convenient shortcut for this that is appropriate for most 
       cases. This is needed so that Flask knows where to look for resources 
       such as templates and static files.

    3. We then use the route() decorator to tell Flask what URL should trigger 
       our function.

    4. The function returns the message we want to display in the user’s browser. 
       The default content type is HTML, so HTML in the string will be rendered 
       by the browser.
       
       
       To run the application, use the flask command or python -m flask. 
       
       You need to tell the Flask where your application is with the --app option.

       flask --app file_name run

'''
