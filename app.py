from flask import Flask, render_template, request
import random

app = Flask(__name__)

opciones = ["piedra", "papel", "tijeras"]

def determinar_ganador(jugador, computadora):
    if jugador == computadora:
        return "empate"
    if (jugador == "piedra" and computadora == "tijeras") or \
       (jugador == "papel" and computadora == "piedra") or \
       (jugador == "tijeras" and computadora == "papel"):
        return "jugador"
    return "computadora"

@app.route("/", methods=["GET", "POST"])
def juego():
    resultado = None
    eleccion_computadora = None
    eleccion_jugador = None

    if request.method == "POST":
        eleccion_jugador = request.form["eleccion"]
        eleccion_computadora = random.choice(opciones)
        resultado = determinar_ganador(eleccion_jugador, eleccion_computadora)

    return render_template("index.html",
        resultado=resultado,
        eleccion_jugador=eleccion_jugador,
        eleccion_computadora=eleccion_computadora
    )

if __name__ == "__main__":
    app.run(debug=True)