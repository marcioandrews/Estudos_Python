from math import*

def subprograma (d1,d2,fp):
  area1 = pi * (d1 / 2) ** 2
  pressao_1 = fp / area1
  area2 = pi * (d2 / 2) ** 2
  pressao_2 = fp / area2
  pressao_2 = pressao_1 / pressao_2
  return pressao_2


def principal():
 d1 = float(input())
 d2 = float(input())
 fp = float(input())
 fpm = float(input())
 pressao_2 = subprograma(d1, d2, fp)

 print (pressao_2)
 
 


principal()
