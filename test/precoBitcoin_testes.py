import unittest
import libnox

class precoBitcoin_testes(unittest.TestCase):
    # Teste unitário de cálculo de Preço de Mercado Estimado Bitcoin para compra
    def test_preco_compra(self):
        precoBitcoin = list()
        precoBitcoin = libnox.preco_Bitcoin(1, 'compra')
        self.assertEqual(precoBitcoin[0],precoBitcoin[1],'Retorno de Valor de compra diferente de Bitcoin e valor de Volume inputado')

    # Teste unitário de cálculo de Preço de Mercado Estimado Bitcoin para compra
    def test_preco_venda(self):
        precoBitcoin = list()
        precoBitcoin = libnox.preco_Bitcoin(1, 'venda')
        self.assertEqual(precoBitcoin[0],precoBitcoin[1],'Retorno de Valor de venda diferente de Bitcoin e valor de Volume inputado')

    # Teste unitário de cálculo de Preço de Mercado Estimado Bitcoin para compra maior que o valor de 1 Bitcoin
    def test_preco_maior_compra(self):
        precoBitcoin = list()
        precoBitcoin = libnox.preco_Bitcoin(3.255, 'compra')
        self.assertGreater(precoBitcoin[1],precoBitcoin[0],'Retorno de Valor de Volume é inferior ao Valor do Bitcoin para compra')

    # Teste unitário de cálculo de Preço de Mercado Estimado Bitcoin para venda maior que o valor de 1 Bitcoin
    def test_preco_maior_venda(self):
        precoBitcoin = list()
        precoBitcoin = libnox.preco_Bitcoin(2.763, 'venda')
        self.assertGreater(precoBitcoin[1],precoBitcoin[0],'Retorno de Valor de Volume é inferior ao Valor do Bitcoin para venda')

    # Teste unitário de cálculo de Preço de Mercado Estimado Bitcoin para compra menor que o valor de 1 Bitcoin
    def test_preco_menor_compra(self):
        precoBitcoin = list()
        precoBitcoin = libnox.preco_Bitcoin(0.0563, 'compra')
        self.assertLess(precoBitcoin[1],precoBitcoin[0],'Retorno de Valor de Volume é superior ao Valor do Bitcoin para compra')

    # Teste unitário de cálculo de Preço de Mercado Estimado Bitcoin para venda menor que o valor de 1 Bitcoin
    def test_preco_menor_venda(self):
        precoBitcoin = list()
        precoBitcoin = libnox.preco_Bitcoin(0.30781, 'venda')
        self.assertLess(precoBitcoin[1],precoBitcoin[0],'Retorno de Valor de Volume é superior ao Valor do Bitcoin para compra')

if __name__ == '__main__':
    unittest.main()