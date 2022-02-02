from app.controllers.controller import ControllerBase
from flask import render_template

class IndexController(ControllerBase):
    @staticmethod
    def get():
        name = "Keith"
        return render_template('index.html',name=name)