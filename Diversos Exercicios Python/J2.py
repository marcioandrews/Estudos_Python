senha = "703456"
tentativas = 0
acerto = 0

while senha != acerto and tentativas < 5:
    acerto = str(input())
    tentativas += 1

    if senha == acerto:
        print('pagou ' + str(tentativas))

    elif tentativas > 5:
        print('nao ' + str(tentativas))