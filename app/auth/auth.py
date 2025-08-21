from flask import render_template, abort
from . import autenticar
from flask import request, redirect, url_for

from datetime import date
from datetime import datetime



@autenticar.route('/login')
def login():
    return render_template('login.html')