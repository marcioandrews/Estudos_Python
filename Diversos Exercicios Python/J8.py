def subprograma (entrada):
  contador = 0
  juntar_letras = ""
  while contador <= len(entrada):
    if contador % 2 != 0:
      juntar_letras += entrada[contador]
    contador += 1
  return juntar_letras


def principal():
  entrada = subprograma(str (input()))
  print (entrada)

principal()
