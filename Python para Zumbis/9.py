km = int (input ('Quantidade de km percorrido '))
d = int (input ('Quantidade de dias '))
pkm = 0.15
pd = 60

total = (km * pkm) + (d * pd)

print (f'Preço a pagar R${total: .2f}')