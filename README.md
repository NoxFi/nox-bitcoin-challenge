 # Desafio Nox Bitcoin
 Aplicativo para listar livro de ofertas de ordens de compra e venda e calcular o valor de preço de mercado estimado
 de compra e venda da criptomoeda Bitcoin, utilizando os valores do livro de ofertas de ordens do site Mercado Bitcoin 
 e calcular a média ponderada entre os preços e quantidade sendo ofertadas para definir o valor de preço de mercado estimado.

 # Como executar o Aplicativo
  
 1 - API para listar ordebook, Livro de ofertas de ordens de compra e venda do Mercado Bitcoin.
 
	1.1 - Execução da API
	COMANDO: ..\NoxBitcoin\code\venv\Scripts\python.exe ../NoxBitcoin/code/api_valor_bitcoin.py
	
	1.2 - Abrir o Browser \ Navegador (hrome, Internet Explorer, Microsoft Edge etc.) e inserir o endereço
	abaixo:
	ENDEREÇO: http://localhost:2000/nox/orderbook/
	
	1.3 - Abrir o Browser \ Navegador (hrome, Internet Explorer, Microsoft Edge etc.) e inserir o endereço 
	abaixo passando	parâmetros de volume e tipo de ordem (compra / venda) para cacular o preço de mercado
	estimado:
	ENDEREÇO: http://localhost:2000/nox/precomercado/10.9&compra
		
 2 - Módulo para calcular o preço de mercado estimado do Bitcoin para compra ou venda.
 
 	2.1 - Execução do módulo
	COMANDO: ..\NoxBitcoin\code\venv\Scripts\python.exe ../NoxBitcoin/code/calculaPreco.py
	
 	2.2 - Digite o volume\quantidade de Bitcoin para calcular o valor de preço de mercado estimado.
	EXEMPLO: 
	"Entre com o Volume de Bitcoin para Ordem: 0.2328"
	
 	2.3 - Digite a opção de tipo de ordem para calcular o valor de preço de mercado estimado ,as opções são 
	(1) para compra e (2) para venda.
	EXEMPLO:
	"Entre com a Opção de Ordem:"
	"[1] - Compra"
	"[2] - Venda"
	"Opção: 1" 
