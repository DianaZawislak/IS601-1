"""A simple flask web app"""
from flask import Flask, render_template
from controllers.index_controller import IndexController
from werkzeug.debug import DebuggedApplication
from controllers.about_controller import AboutController

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.wsgi_app = DebuggedApplication(app.wsgi_app, True)


@app.route("/", methods=['GET'])
def index_get():
    return IndexController.get()

@app.route("/about", methods=['GET'])
def about_get():
    return AboutController.get()
