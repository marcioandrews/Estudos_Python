m = int(input("Quantos minutos você consumiu?  "))

if m < 200:
	print ('Sua conta será de R$', (m*0.20))

if m >= 200 and m < 400:
	print ('Sua conta será de R$', (m*0.18))

if m >= 400 and m < 800:
	print ('Sua conta será de R$', (m*0.15))

if m >= 800:
	print ('Sua conta será de R$', (m*0.08))
