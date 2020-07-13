from math import floor

def subprograma (a):
  if a % 2 == 0:
    a = (floor(a))

  else:
    a = (floor(a))
    if a % 2 == 0:
      a += 1
  return a


def principal():
  entrada = subprograma(float (input()))
  print (entrada)

principal()
