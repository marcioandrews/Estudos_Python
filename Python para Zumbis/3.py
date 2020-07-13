d = int (input ('Dia '))
h = int (input ('Horas '))
m = int (input ('Minutos '))
s = int (input ('Segundos '))
total = 0
d = d * 24
h = h + d
h = h * 60
m = m + h
m = m * 60
s = s + m

total = s

print (total)