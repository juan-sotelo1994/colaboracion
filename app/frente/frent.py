from flask import render_template 
from . import frente

@frente.route('/', endpoint='inicio')
def index():
    return render_template("inicio.html")