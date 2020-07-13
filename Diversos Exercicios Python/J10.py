def ordenar (nomecompleto1, nomecompleto2):
  loop = 0
  ordem = ""
  while loop <= len(nomecompleto1):
    if nomecompleto1[loop] < nomecompleto2[loop]:
      ordem = nomecompleto1 + "\n" + nomecompleto2
      break
    if nomecompleto1[loop] > nomecompleto2[loop]:
      ordem = nomecompleto2 + "\n" + nomecompleto1
      break
    loop += 1
    
  return ordem


def separador (nome):
 nome, sobrenome = map(str, nome.split())
 nomecompleto = sobrenome + ", " + nome[0] + "."
 return nomecompleto


def principal():
 nomecompleto1 = separador (str (input()))
 nomecompleto2 = separador(str (input()))
 ordemalfabetica = ordenar(nomecompleto1, nomecompleto2)

 print (ordemalfabetica)
 

principal()
