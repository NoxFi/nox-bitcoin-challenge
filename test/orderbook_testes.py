import unittest
import libnox
import json

class orderbook_testes(unittest.TestCase):
    # Teste unitário de retorno de lista de Livro de Ofertas
    def test_listas(self):
        dadosBitcoin = dict()
        dadosBitcoin = json.loads(libnox.orderbook())
        resultado=len(dadosBitcoin)
        self.assertEqual(3,resultado,'Retorno de lista Livro de Ofertas Incorreta')

    # Teste unitário de retorno de lista de Livro de Ofertas de compra
    def test_bids(self):
        dadosBitcoin = dict()
        dadosBitcoin = json.loads(libnox.orderbook())
        resultado=len(dadosBitcoin['bids'])
        self.assertEqual(1000,resultado,'Retorno de Livro de ordens de compra Incorreta')

    # Teste unitário de retorno de lista de Livro de Ofertas de venda
    def test_asks(self):
        dadosBitcoin = dict()
        dadosBitcoin = json.loads(libnox.orderbook())
        resultado=len(dadosBitcoin['asks'])
        self.assertEqual(1000, resultado, 'Retorno de Livro de ordens de venda Incorreta')

if __name__ == '__main__':
    unittest.main()