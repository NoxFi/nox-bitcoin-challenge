import os
import requests
import libnox
from flask import Flask, jsonify, request
from time import sleep
app = Flask(__name__)


@app.route('/nox/orderbook/', methods=['GET'])
def orderbook():
    return libnox.orderbook('BTC')


@app.route('/nox/precomercado/<volume>&<tipo>', methods=['GET'])
def precomercado(volume, tipo):
    precoAtual = list()
    precoAtual = libnox.preco_Bitcoin(float(volume), str(tipo))
    return jsonify(
        tipo=tipo,
        volume=float(volume),
        valor_bitcoin=precoAtual[0],
        valor_volume=precoAtual[1]
    )


app.run(host="0.0.0.0", port = 2000, debug = False)
