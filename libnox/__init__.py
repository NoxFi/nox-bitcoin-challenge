import requests
import json
from time import sleep

def orderbook(coin='BTC'):
    """
    Função para extrair orderbook do mercadobitcoin e disponibilizar as informações de livro Ofertas de compra e venda
    :param coin:
        Descrição: Acrônimo da moeda digital
        Tipo: String
        Domínio de dados:
            ASRFT : Fan Token ASR
            ATMFT : Fan Token ATM
            BCH : Bitcoin Cash
            BTC : Bitcoin
            CAIFT : Fan Token CAI
            CHZ : Chiliz
            ETH : Ethereum
            GALFT : Fan Token GAL
            IMOB01 : None
            JUVFT : Fan Token JUV
            LINK : CHAINLINK
            LTC : Litecoin
            MBCONS01 : Cota de Consórcio 01
            MBCONS02 : Cota de Consórcio 02
            MBFP01 : None
            MBPRK01 : Precatório MB SP01
            MBPRK02 : Precatório MB SP02
            MBPRK03 : Precatório MB BR03
            MBPRK04 : Precatório MB RJ04
            MBVASCO01 : MBVASCO01
            PAXG : PAX Gold
            PSGFT : Fan Token PSG
            USDC : USD Coin
            WBX : WiBX
            XRP : XRP
    :return: json com últimas 1000 ordens de compra e de venda do mercadobitcoin
    """
    request = requests.get(f"https://www.mercadobitcoin.net/api/{coin}/orderbook")
    return request.content


def valorEstimado(tipoTransacao):
    dadosBitcoin = dict()
    dadosBitcoin = json.loads(orderbook('BTC'))
    qtde = 0
    soma = 0
    # Listar Dados de livro Ofertas de Compra
    if tipoTransacao == 'compra':
        for i in dadosBitcoin['bids']:
            soma += i[0] * i[1]
            qtde += i[1]
    # Listar Dados de livro Ofertas de Venda
    elif tipoTransacao == 'venda':
        for i in dadosBitcoin['asks']:
            soma += i[0] * i[1]
            qtde += i[1]
    return  soma / qtde


def preco_Bitcoin(qtdeBitcoin, tipoTransacao):
    valorBitcoin = valorEstimado(tipoTransacao)
    if tipoTransacao == 'compra':
        valorOrdem = qtdeBitcoin * valorBitcoin
    elif tipoTransacao == 'venda':
        valorOrdem = qtdeBitcoin * valorBitcoin

    return [valorBitcoin,valorOrdem]

