# api desafio do processo seletivo da empresa NoxBitcoin
# 1 - Serviço para listar Livro de Ofertas de ordens de compra e venda de Bitcoin
import os
import requests
import libnox
from flask import Flask, jsonify, request
from time import sleep
app = Flask(__name__)

#Rota para listar Livro de Ofertas de compra e venda de Bitcoin
@app.route('/nox/orderbook/', methods=['GET'])
def orderbook():
    return libnox.orderbook()

#Rota para calcular Preco de Mercado Estimado para Bitcoin de compra e venda
@app.route('/nox/precomercado/<volume>&<tipo>', methods=['GET'])
def precomercado(volume, tipo):
    precoAtual = list()
    try:
        precoAtual = libnox.preco_Bitcoin(float(volume), str(tipo))
        return jsonify(
            tipo=tipo,
            volume=float(volume),
            valor_bitcoin=precoAtual[0],
            valor_volume=precoAtual[1]
        )
    except:
        return jsonify(erro='Erro no Calculo de Preco de Mercado Estimado')


app.run(host="0.0.0.0", port = 2000, debug = False)
