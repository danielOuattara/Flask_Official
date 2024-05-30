from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello World of Flask !</p>"

# flask --app file_name run --debug
