import os
from flask import Flask, jsonify, request
from math import sqrt

app = Flask(__name__)


@app.route('/')
def nao_entre_em_panico():

    prox = 1
    ante = 0

    resposta = str(ante)+", "+str(prox)+", "

    for a in range(1, 50-1):
        new = prox
        prox = prox + ante
        ante = new
        resposta += str(prox)+", "


    return resposta

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
