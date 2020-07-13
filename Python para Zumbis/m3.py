x, y, z = map(int, input('Informe os lados do triângulo separados por ,').split())

if x + y >= z:
	if x == y and x == z:
		print('Triangulo equilatero')
	if x == y and z < x or z > x:
		print('triangulo isosceles')
	if x < y or x > y and z < x or z > x:
		print('triangulo escaleno')
else:
	print('Não é um triangulo')