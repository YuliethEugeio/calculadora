from flask import Flask
from flask_cors import CORS
import math as st  
from flask import jsonify

app = Flask(__name__)
CORS(app)

# Ruta para la suma
@app.route("/")
@app.route("/<float:numero1>/<float:numero2>")
@app.route("/<int:numero1>/<int:numero2>")
@app.route("/<int:numero1>/<float:numero2>")
@app.route("/<float:numero1>/<int:numero2>")
def suma(numero1=0, numero2=0):
    resultado = numero1 + numero2




    # Retornamos un objeto JSON
    data = {
        "Resultado": resultado,
        "Operacion": "suma"
    }
    return jsonify(data)

# Resta
@app.route("/resta/<float:numero1>/<float:numero2>")
@app.route("/resta/<int:numero1>/<int:numero2>")
@app.route("/resta/<int:numero1>/<float:numero2>")
@app.route("/resta/<float:numero1>/<int:numero2>")
def resta(numero1=0, numero2=0):
    resultado = numero1 - numero2 


    

    # Retornamos un objeto JSON
    data = {
        "Resultado": resultado,
        "Operacion": "resta"
    }
    return jsonify(data)

# Multiplicación
@app.route("/multiplicacion/<float:numero1>/<float:numero2>")
@app.route("/multiplicacion/<int:numero1>/<int:numero2>")
@app.route("/multiplicacion/<int:numero1>/<float:   numero2>")
@app.route("/multiplicacion/<int:numero1>/<float:numero2>") 

def multiplicacion(numero1=0, numero2=0):
    resultado = numero1 * numero2 




    # Retornamos un objeto JSON
    data = {
        "Resultado": resultado,
        "Operacion": "multiplicacion"
    }
    return jsonify(data)

# División
@app.route("/division/<float:numero1>/<float:numero2>")
@app.route("/division/<int:numero1>/<int:numero2>")
@app.route("/division/<int:numero1>/<float:numero2>")
@app.route("/division/<float:numero1>/<int:numero2>")
def division(numero1=0, 
 numero2=0):
    if numero2 == 0:
        return jsonify({"error": "No se puede dividir por cero"})
    resultado = numero1 / numero2

    

    # Retornamos un objeto JSON
    data = {
        "Resultado": resultado,
        "Operacion": "División"
    }
    return jsonify(data)

# Potenciación
@app.route("/potenciacion/<float:numero1>/<float:numero2>")
@app.route("/potenciacion/<int:numero1>/<int:numero2>") 

@app.route("/potenciacion/<int:numero1>/<float:numero2>")
@app.route("/potenciacion/<float:numero1>/<int:numero2>")
def potenciacion(numero1=0, numero2=0):
    resultado = numero1 ** numero2 


   

    # Retornamos un objeto JSON
    data = {
        "Resultado": resultado,
        "Operacion": "potenciación"
    }
    return jsonify(data)

