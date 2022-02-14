from flask import render_template
#don't change this import or it can't find the module controller
from  . controller import ControllerBase


class IndexController(ControllerBase):
    @staticmethod
    def get():
        name = "Mauricio AlarcoHildebrandt"
        return render_template('/static/html/index.html', name=name)
