porcentagem = float(input())
mes = int (input())
quant_loop = 1
total = 0
porcentagem = porcentagem / 100

while quant_loop <= mes:
	deposito = float(input())
	total += deposito
	total = total + total * porcentagem
	quant_loop = quant_loop + 1

print (total)