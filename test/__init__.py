# Executar todos casos de testes unitários
from unittest import TestLoader, TextTestRunner, TestSuite
from test.orderbook_testes import orderbook_testes
from test.precoBitcoin_testes import precoBitcoin_testes
from test.valorEstimado_testes import valorEstimado_testes

if __name__ == "__main__":

    loader = TestLoader()
    tests = [
        loader.loadTestsFromTestCase(test)
        for test in (orderbook_testes, precoBitcoin_testes, valorEstimado_testes)
    ]
    suite = TestSuite(tests)

    runner = TextTestRunner(verbosity=2)
    runner.run(suite)