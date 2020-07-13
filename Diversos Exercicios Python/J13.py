loop, numero_atual = map(int, input().split())
contador = 0
primo = True
divisor = 2

while loop < numero_atual:
	divisor = 2
	primo = True
	while divisor < loop:
		if loop % divisor == 0:
			primo = False
		if primo:
			contador += 1
			divisor += loop
		divisor += 1
	loop += 1
print (contador)