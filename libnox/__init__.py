import requests
import json

def orderbook():
    """
    Função para extrair orderbook do mercadobitcoin e disponibilizar as informações de livro de Ofertas de compra e venda
    :return: json com as últimas 1000 ordens de compra e de venda do Livro de Ofertas do mercadobitcoin
    """
    request = requests.get(f"https://www.mercadobitcoin.net/api/BTC/orderbook")
    return request.content


def valorEstimado(tipoTransacao):
    """
    Função para calcular a média ponderada do Livro de Ofertas de ordens de compra e venda disponibilizado pela api do Mercado Bitcoin
    :param tipoTransacao: o parâmetro deve ser 'compra' ou 'venda' para definir qual Livro de Ofertas será utilizado para o cálculo da média ponderada
    :return: retorna o valor da média ponderada do valor do Bitcoin de acordo com o Livro de Ofertas de ordens de compra e venda
    """
    dadosBitcoin = dict()
    dadosBitcoin = json.loads(orderbook())
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
    """
    Função para calcular o Preço de Mercado Estimado para o Bitcoin
    :param qtdeBitcoin: Volume de Bitcoin para calcular o Preço de Mercado Estimado
    :param tipoTransacao: o parâmetro deve ser 'compra' ou 'venda' para definir qual Livro de Ofertas será utilizado para o
                          cálculo do Preço de Mercado Estimado
    :return: Preço de Mercado Estimado para 1 Bitcoin e Preço de Mercado Estimado para o volume de input
    """
    valorBitcoin = valorEstimado(tipoTransacao)
    if tipoTransacao == 'compra':
        valorOrdem = qtdeBitcoin * valorBitcoin
    elif tipoTransacao == 'venda':
        valorOrdem = qtdeBitcoin * valorBitcoin
    return [valorBitcoin,valorOrdem]


def input_Float(texto='Entre com Valor: '):
    """
    :param texto: Texto de mensagem para input do valor numérico
    :return: valor numérico validado
    """
    while True:
        svalor = str(input(texto)).replace(',', '.')
        try:
            valor = float(svalor)
            break
        except:
            print('\033[31mERRO: Digite um valor numérico válido.\033[m')
    return valor
