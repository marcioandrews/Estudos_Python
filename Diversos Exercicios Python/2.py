def principal():
    
    lse, lie = map (float, input().split())
    desvio = float (input ())
    mediana = float (input ())
    cpk = 0

    if (lse - mediana) / (3 * desvio) < (mediana - lie) / (3 * desvio):
        cpk = (lse - mediana) / (3 * desvio)
    if (lse - mediana) / (3 * desvio) > (mediana - lie) / (3 * desvio):
        cpk = (mediana - lie) / (3 * desvio)
    print (f'{cpk:.2f}')

    if cpk > 1.33:
        print ('Capaz')
    if cpk <= 1.33 and cpk > 1.0 :
        print ('Satisfatorio')
    if cpk < 1.0:
        print ('Incapaz')
principal()
