"""A simple flask web app"""
from flask import Flask
from werkzeug.debug import DebuggedApplication

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.wsgi_app = DebuggedApplication(app.wsgi_app, True)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
