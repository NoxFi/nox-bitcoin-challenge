#Programa calculaPreco desafio Nox Bitcoin vs 1.0.1

import libnox
from time import sleep
from datetime import datetime

print('\033[33m{}'.format('=' * 70))
print(f'{"Calcular Preço a Mercado Estimado de Bitcoin":^70}')
print('\033[33m{}\033[m'.format('=' * 70))

precoAtual = list()
qtdOrdem = libnox.input_Float('Entre com o Volume de Bitcoin para Ordem: ')

while True:
    print ('Entre com a Opção de Ordem:')
    print ('\033[33m[1]\033[m - Compra')
    print ('\033[33m[2]\033[m - Venda')
    tipoOrdem = str(input('Opção: ')).strip()[0]
    if tipoOrdem in '12':
        if tipoOrdem == '1':
            tipoOrdem = 'compra'
        elif tipoOrdem == '2':
            tipoOrdem = 'venda'
        break
    else:
        print('\033[31mERRO : Opção inválida, por favor digite novamente.\033[m')

while True:
    precoAtual = libnox.preco_Bitcoin(qtdOrdem,tipoOrdem)
    print('\033[33m{}\033[m'.format('='*70))
    print(f'Data / Hora: \033[33m{datetime.now().strftime("%d/%m/%Y %H:%M:%S")}\033[m')
    print(f'Tipo de Ordem: \033[33m{tipoOrdem}\033[m')
    print(f'Preço a Mercado Estimado de 1.00000000 Bitcoin: \033[33mR$ {precoAtual[0]:.2f}\033[m')
    print(f'Preço a Mercado Estimado de {qtdOrdem:.8f} Bitcoin: \033[33mR$ {precoAtual[1]:.2f}\033[m')
    print('\033[33m{}\033[m'.format('='*70))
    sleep(3)




