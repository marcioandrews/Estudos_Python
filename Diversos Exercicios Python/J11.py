def transformar(nome1, nome2):
 nome1, sobrenome = map(str, nome1.split())
 nomecompleto1 = sobrenome + ", " + nome1[0] + "."
 nome2, sobrenome2 = map(str, nome2.split())
 nomecompleto2 = sobrenome2 + ", " + nome2[0] + "."
 loop = 0
 ordem = ""
 while loop <= len(nomecompleto1):
    if nomecompleto1[loop] < nomecompleto2[loop]:
      ordem = nomecompleto1 + "\n" + nomecompleto2
      loop += len(nomecompleto1)
    elif nomecompleto1[loop] > nomecompleto2[loop]:
      ordem = nomecompleto2 + "\n" + nomecompleto1
      loop += len(nomecompleto1)
    loop += 1
 return ordem


def principal():
 nomecompleto1= str (input())
 nomecompleto2 = str (input())
 ordemalfabetica = transformar(nomecompleto1, nomecompleto2)

 print (ordemalfabetica)
 

principal()
