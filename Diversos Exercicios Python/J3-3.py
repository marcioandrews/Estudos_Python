def principal():
    entrada = str(input())
    pes = float(input())
    alt = float(input())
    imc = pes/alt**2

    if entrada == 'h':
        if imc <= 20.7:
            print('abaixo do peso')
        elif imc > 20.7 and imc <= 26.4:
            print('no peso ideal')
        elif imc > 26.4 and imc <= 27.8:
            print('pouco acima do peso')
        elif imc > 27.8 and imc <= 31.1:
            print('acima do peso')
        else:
            print('obesidade')
    else:
        if imc <= 19.1:
            print('abaixo do peso')
        elif imc > 19.1 and imc <= 25.8:
            print('no peso ideal')
        elif imc > 25.8 and imc <= 27.3:
            print('pouco acima do peso')
        elif imc > 27.3 and imc <= 32.3:
            print('acima do peso')
        else:
            print('obesidade')
principal()