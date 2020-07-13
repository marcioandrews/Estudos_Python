entrada = int(input()) # entrada do numero de vezes que vao aparecer os primos
numero_atual = 1 # numero crescente 
divisor = 2
primo = True
loop = 7 # loop de vezes que da certo o numeor primo

while loop < entrada:
	primo = True # aqui estou resetando o true
	numero_atual += 1
	divisor = 2 # aqui estou resetando o divisor
	while divisor < numero_atual:
		if numero_atual % divisor == 0:
			primo = False
		divisor += 1
	if primo:
		loop += 1
		print (numero_atual)
	

		
	

