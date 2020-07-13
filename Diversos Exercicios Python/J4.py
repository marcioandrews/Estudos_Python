qpalavras = int(input()) #entrada numero de palavras
contador = 0 #contador do segundo While
letra = 0 #armazenar as letras separadas da entrada
qtd_vogais = 0 #armazenar o numero de vogais da palavra
contador3 = 0 #contador do primeiro While
maiorvogal = 0 #armazenar a palavra com maior quantidade de vogais
nomeimp = 0 #armazenar o nome da palavra com mais vogais
while contador3 < qpalavras:
	entrada = str(input())
	contador3 += 1
	contador = 0

	while contador < len(entrada): 
		letra = entrada[contador]
		contador += 1

		if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
				qtd_vogais += 1


	if qtd_vogais >= maiorvogal:
		maiorvogal = qtd_vogais
		nomeimp = entrada

	
	qtd_vogais = 0

print (nomeimp)