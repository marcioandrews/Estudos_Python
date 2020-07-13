def principal():
    troco = int(input())
    nota = int(input())
    n1 = 0
    n5 = 0
    n10 = 0
    n20 = 0
    n50 = 0

    if nota == 50:
        if troco >= 20:
            n20 = troco // 20
            troco = troco % 20
        if troco >= 10:
            n10 = troco // 10
            troco = troco % 10
        if troco >= 5:
            n5 = troco // 5
            troco = troco % 5
        else:
            n1 = troco // 1
            troco = troco % 1
        print (f' 1: {n1:}')
        print (f' 5: {n5:}')
        print (f' 10: {n10:}')
        print (f' 20: {n20:}')
        
    else:
        if troco >= 50:
            n50 = troco // 50
            troco = troco % 50
        if troco >= 10:
            n10 = troco // 10
            troco = troco % 10
        if troco >= 5:
            n5 = troco // 5
            troco = troco % 5
        else:
            n1 = troco // 1
            troco = troco % 1
        
        print (f' 1: {n1:}')
        print (f' 5: {n5:}')
        print (f' 10: {n10:}')
        print (f' 50: {n50:}')
principal()