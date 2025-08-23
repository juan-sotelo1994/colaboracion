from flask import render_template, abort
import mysql.connector

def obtener_conexion():
    try:
        mydb = mysql.connector.connect(
            host ="localhost",
            user ="root",
            password ="",
            db = "radiologia_citas"
            )
    except Exception:
        abort(500)
    return mydb
              