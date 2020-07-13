v = int(input("Qual a velocidade do carro?  "))


if v > 110:
	print ('O usuario foi multa do em R$', (v - 110)*5)

else:
	print ("O usuario não foi multado") 
