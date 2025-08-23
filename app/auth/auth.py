from flask import render_template, abort
from . import autenticar
from flask import request, redirect, url_for

from datetime import date
from datetime import datetime


@autenticar.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        correo = request.form['correo']
        password = request.form['password']

        # Aquí validas usuario y contraseña en la BD
        # if valido:
        return render_template('administrador/iniciopanel.html')

    return render_template("login.html")

@autenticar.route('/recupera')
def recupera():
    return render_template('/recupera1.html')

@autenticar.route('/verificar', methods=['GET'])
def verificar():
    return render_template('recupera2.html')

@autenticar.route('/validar', methods=['GET'])
def validar():
    return render_template('recupera3.html')
