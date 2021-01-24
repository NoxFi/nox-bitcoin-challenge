#Programa desafio Nox Bitcoin vs 1.0.0

import libnox
from time import sleep
import sys
import _thread


precoAtual = list()


qtdOrdem = float(input('Quantidade de Bitcoin: '))
print ('Opção de Ordem:')
print ('[1] - Compra')
print ('[2] - Venda')

tipoOrdem = str(input('Opção: ')).strip()[0]
if tipoOrdem == '1':
    tipoOrdem = 'compra'
elif tipoOrdem == '2':
    tipoOrdem = 'venda'


while True:
    precoAtual = libnox.preco_Bitcoin(qtdOrdem,tipoOrdem)
    print('='*60)
    print(f'Preço a Mercado Estimado {tipoOrdem} de 1 Bitcoin: R$ {precoAtual[0]:.2f}')
    print(f'Preço a Mercado Estimado {tipoOrdem} de {qtdOrdem} Bitcoin: R$ {precoAtual[1]:.2f}')
    print('='*60)
    sleep(30)


#print(f'{libnox.preco_Bitcoin(1, "venda")[0]:.2f}')




