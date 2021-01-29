import unittest
import libnox

class valorEstimado_testes(unittest.TestCase):
    # Teste unitário de retorno de valor de Bitcoin para compra
    def test_valor_compra(self):
        resultado=libnox.valorEstimado('compra')
        self.assertGreater(resultado,0,'Retorno de Valor de compra inferior a 0')

    # Teste unitário de retorno de valor de Bitcoin para venda
    def test_valor_venda(self):
        resultado=libnox.valorEstimado('venda')
        self.assertGreater(resultado,0,'Retorno de Valor de venda inferior a 0')

    # Teste unitário para comparar preço de venda com preço de compra
    def test_comparar_compra_venda(self):
        vlcompra = libnox.valorEstimado('compra')
        vlvenda=libnox.valorEstimado('venda')
        self.assertGreater(vlvenda,vlcompra,'Retorno de Valor de Compra maior que de Venda')

if __name__ == '__main__':
    unittest.main()