dias = int(input())
v = 343 # velocidade do som
p = float(input()) # distancia entre o fundo do curso da agua e o linigrafo
limite_superior = float(input())
limite_inferior = float(input())
t = 0
y = 0
loop = 1
media = 0
nivel_agua_dia = ""
altura_max = 0
altura_min = 0

while loop <= dias:
	t = float(input()) # tempo de resposta de cada dia
	y = p - (v * t) / 2 # altura do nivel da agua
	media += y # media somando com ela mesma para depois dividir por dias

	if loop == 1: # transformando as variaveis altura max e altura min em y para depois descobrir o maior e o menor valor
		altura_max = y
		altura_min = y

	nivel_agua_dia += "Dia " + str(loop) + ": " + str('{:.2f}'.format(y))
	if loop != dias: # enquanto os loop for diferente dos dias sera concatenado 1 quebra de linha
		nivel_agua_dia += "\n"
	loop += 1
	
# continuaçao para saber o maior e menor valor
	if altura_max < y:
		altura_max = y

	if altura_min > y:
		altura_min = y
	
media = media / dias

print (nivel_agua_dia)
print ('{:.2f}'.format(media))
print ('{:.2f}'.format(altura_max))
print ('{:.2f}'.format(altura_min))

if media < limite_inferior:
	print ("Risco de escassez hidrica")

if media > limite_superior:
	print ("Risco de enchente")