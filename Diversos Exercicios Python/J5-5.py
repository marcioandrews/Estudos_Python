def principal():
    n1,n2,produto = map(str,input().split())
    p1,p2,p3 = map(int,input().split())
    q1 = int (input())
    q2 = int(input())
    r1 = q1/p1
    r2 = q2/p2

    if r1 > r2:
        exc = r1 - r2
    else:
        exc = r2 - r1

    if r1 < r2:
        p = r1 * p3
    else:
        p = r2 * p3
    
    if r1 < r2:
        rea = n2
    if r1 > r2:
        rea = n1
    if r1 == r2:
        rea = 0

    print (f'Reagente em excesso: {rea:}')
    print (f'Excesso: {exc:}')
    print (f'Produto: {p:} {produto}')
principal()