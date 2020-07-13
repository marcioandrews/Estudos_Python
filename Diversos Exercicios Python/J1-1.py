def principal():
    x = float(input())
    y = float(input())
    i = float(input())
    j = float(input())
    d = ((x-i)**2+(j-y)**2)**0.5

    if d <= 300:
        print('ACERTOU')
    else:
        print(d)

principal()