qc = int (input ('Quantidade de cigarros fumados por dia '))
af = int (input ('Anos fumando '))
totala = af * 365
totalc = qc * totala
total = totalc / 1440
print (f'{total:.2f}')