from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def index():
    return "<p>Enter anything in the address bar after the \"/\" </p>"


@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"


# flask --app file_name run
"""
When returning HTML (the default response type in Flask), 
any user-provided values rendered in the output must be 
escaped to protect from injection attacks. 

HTML templates rendered with Jinja, introduced later, 
will do this automatically.

`escape()`, shown here, can be used manually. It is omitted 
in most examples for brevity, but you should always be aware 
of how you're using untrusted data.

If a user managed to submit the name <script>alert("bad")</script>, 
escaping causes it to be rendered as text, rather than running 
the script in the user’s browser.

<name> in the route captures a value from the URL and passes 
it to the view function. These variable rules are explained below.

"""
