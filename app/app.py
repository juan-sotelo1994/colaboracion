from flask import Flask, render_template, request
import os 

app = Flask(__name__)

# resgistro de las importaciones y configuraciones 
from frente import frente
from auth import autenticar

# Registro de blueprints

app.register_blueprint(frente)
app.register_blueprint(autenticar)




# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True, port=5711)
