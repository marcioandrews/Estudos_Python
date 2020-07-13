def principal():
    
    x = int (input ())
    v1 = 0
    v2 = 0
    v3 = 0
    v4 = 0
    v5 = 0
    d2 = 0
    d3 = 0
    d23 = 0

    v5 = x % 10

    x = x // 10
    
    v4 = x % 10

    x = x // 10

    v3 = x % 10

    x = x // 10

    v2 = x % 10

    x = x // 10

    v1 = x % 10

    if v5 % 2 == 0:
        d2 = d2 + 1
    if v4 % 2 == 0:
        d2 = d2 + 1
    if v3 % 2 == 0:
        d2 = d2 + 1
    if v2 % 2 == 0:
        d2 = d2 + 1
    if v1 % 2 == 0:
        d2 = d2 + 1

    if v5 % 3 == 0:
        d3 = d3 + 1
    if v4 % 3 == 0:
        d3 = d3 + 1
    if v3 % 3 == 0:
        d3 = d3 + 1
    if v2 % 3 == 0:
        d3 = d3 + 1
    if v1 % 3 == 0:
        d3 = d3 + 1

    if v5 % 2 == 0 and v5 % 3 == 0:
        d23 = d23 + 1
    if v4 % 2 == 0 and v4 % 3 == 0:
        d23 = d23 + 1
    if v3 % 2 == 0 and v3 % 3 == 0:
        d23 = d23 + 1
    if v2 % 2 == 0 and v2 % 3 == 0:
        d23 = d23 + 1
    if v1 % 2 == 0 and v1 % 3 == 0:
        d23 = d23 + 1
    print (d2)
    print (d3)
    print (d23)
principal()
