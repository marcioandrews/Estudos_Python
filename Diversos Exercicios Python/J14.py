def principal():
	numero_menor, numero_maior = map(int, input().split())
	contador = 0
	while numero_menor <= numero_maior:
		if primo(numero_menor):
			contador += 1
		numero_menor += 1
	print (contador)



def primo(numero):
	loop = 2
	primo = True
	nao_primo = False
	while loop < numero:
		if numero % loop == 0:
			return nao_primo

		loop += 1
	return primo
	


principal()
