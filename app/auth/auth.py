from flask import render_template, abort
from . import autenticar
from flask import request, redirect, url_for

from datetime import date
from datetime import datetime



@autenticar.route('/login')
def login():
    return render_template('login.html')

@autenticar.route('/recupera')
def recupera():
    return render_template('/recupera1.html')

@autenticar.route('/verificar')
def verificar():
    return render_template('recupera2.html')