from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

def gerar_ano_mes(ano):
    meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
             "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    mes = random.choice(meses)
    return {"ano": ano, "mes": mes}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_data", methods=["POST"])
def get_data():
    data = request.get_json()
    ano = data.get("year")
    resultado = gerar_ano_mes(ano)
    return jsonify(resultado)
