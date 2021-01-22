# Desafio Nox Bitcoin

Nosso desafio será tanto uma avaliação técnica, quanto a sua capacidade de entender um domínio de problema.

## Domínio do problema

Como somos uma empresa que negocia bitcoins, pediremos para você criar um sistema de cálculo de preço do bitcoin na exchange Mercado Bitcoin. 

O sistema deverá ter apenas 2 inputs*: A quantidade de bitcoins a ser negociada, e o tipo de negociação (compra ou venda).
![exemplo](https://user-images.githubusercontent.com/16902401/105039468-5a56a780-5a3f-11eb-9f28-c8b7a1da774a.PNG)

O sistema deverá calcular o preço a mercado estimado do bitcoin para os inputs solicitados.

É isso!

_*Imagem ilustrativa. Não será necessário interface gráfica_




Confundiu tudo? Não se preocupe, nós explicamos para você!
![orderbook](https://user-images.githubusercontent.com/16902401/105074225-dadcce80-5a66-11eb-9e41-e05586f01949.jpg)

https://www.mercadobitcoin.com.br/plataforma/painel/crypto/btc

## Desafio

Vamos dividir o sistema em duas partes:

A primeira parte é construir uma API, que possuirá um endpoint de consulta de orderbook.
Utilize a api rest da Mercado Bitcoin: https://www.mercadobitcoin.com.br/api-doc/

Na segunda parte você precisa criar um módulo que cálcula o preço do bitcoin a partir dos inputs:
 - Volume (quantidade a ser negociada de bitcoins)
 - Tipo de operação (compra ou venda)

Para completar o sistema, você precisa seguir alguns passos:

- Obter as informações do orderbook do mercado bitcoin (endpoint https://www.mercadobitcoin.net/api/BTC/orderbook/ da api) 
- Obter as informações de input do usuário
- Calcular e exibir o preço a mercado estimado do bitcoin 
- Atualizar informações a cada 30 segundos


## Requisitos

- Ser escrito em Python ou Go
- Ter testes automatizados
- Forkar esse desafio e criar o seu projeto (ou workspace) usando a sua versão desse repositório, tão logo acabe o desafio, submeta um _pull request_. 

## Critério de avaliação

-   **Organização do código**
-   **Clareza**: O README explica de forma resumida qual é o problema e como pode rodar a aplicação?
-   **Assertividade**: A aplicação está fazendo o que é esperado? Se tem algo faltando, o README explica o porquê?
-   **Legibilidade do código** (incluindo comentários)
-   **Cobertura de testes** (Não esperamos cobertura completa)
-   **Histórico de commits** (estrutura e qualidade)
-   **Usabilidade**: A API é intuitiva?
-   **Escolhas técnicas**: A escolha das bibliotecas, arquitetura, etc, é a melhor escolha para a aplicação?


## Sistemas de referência

- https://biscoint.io/
- https://www.noxbitcoin.com.br/valor-do-bitcoin/

## Dúvidas

Quaisquer dúvidas que você venha a ter, consulte as [_issues_](https://github.com/Nox-Bitcoin/nox-challenge/issues) para ver se alguém já não a fez e caso você não ache sua resposta, abra você mesmo uma nova issue!
