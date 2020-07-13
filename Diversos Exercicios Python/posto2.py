'''Um posto de gasolina e voce pode abastecer com alcool e com gasolina, o preço do alcool é 3reais e a gasolina é 5reais.
A pessoa que for abastecer ela pode falar coloca 5 litros de gasolina pra mim ou ela pode falar coloca 50 reais de gasolina pra mim              
'''
tipo=input("Coloque 'G' para Gasolina e 'A' para Alcool ")
tipo_x=input("Coloque 'L' para Litros e 'D' para Dinheiro ")
quant=int(input("Quantidade"))
va=3
vg=5
valor_total=0
total_litros=0
total_inf=0


if tipo=="G":
	if tipo_x=="L":
		valor_total=quant*vg
		total_litros=quant

	else:
		valor_total=quant
		total_litros=quant/vg


else:
	if tipo_x=="D":
		valor_total=quant
		total_litros=quant/va

	else:
		valor_total=quant*va
		total_litros=quant


print(str(total_litros)+" valor dos litros")
print(str(valor_total)+" valor do dinheiro")