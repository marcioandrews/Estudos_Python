def transformar(nome, sobrenome):
 nomecompleto = sobrenome + ", " + nome[0] + "."

 return nomecompleto


def principal():
 nome1, sobrenome1 = map(str, input().split())
 nomecompleto1 = transformar(nome1, sobrenome1)
 nome2, sobrenome2 = map(str, input().split())
 nomecompleto2 = transformar(nome2, sobrenome2)
 
 if nomecompleto1 < nomecompleto2:
   print (nomecompleto1 + "\n" + nomecompleto2)

 else:
   print (nomecompleto2 + "\n" + nomecompleto1)

principal()
