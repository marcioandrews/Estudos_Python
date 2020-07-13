'''Quero que você faça um programa que receba um Numero N
que vai ser o enezimo numero da sequencia de fibonacci  e imprima ele
                                  x z f
Exemplo de sequencia de fibonacci 0 1 1 2 3 5 8 13 21 34
'''
i=0
y=int(input("numero "))
aant=0
ant=1
fib=0
temp=0

if y==1:
	fib=0

elif y==2:
	fib=1
else:
	while i<y-2:
		temp=fib
		fib=aant+ant
		aant=ant
		ant=fib
		i=i+1

print(fib)