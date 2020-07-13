def principal():
    car = str (input())
    r1 = str (input())
    r2 = str (input())
    r3 = str (input())
    uno = 30100.5
    palio = 32550.2
    fiorino = 40400.0
    som = 599.9
    ar = 859.9
    dvd = 950.9

    if car == 'UNO':
        if r1 == 'NAO' and r2 == 'NAO' and r3 == 'SIM':
            uno = uno + dvd
            print (f'DVD')
            print (f'{uno:.1f}')
        if r1 == 'NAO' and r2 == 'SIM' and r3 == 'NAO':
            uno = uno + ar
            print (f'AR')
            print (f'{uno:.1f}')
        if r1 == 'SIM' and r2 == 'NAO' and r3 == 'NAO':
            uno = uno + som
            print (f'SOM')
            print (f'{uno:.1f}')
        if r1 == 'NAO' and r2 == 'SIM' and r3 == 'SIM':
            uno = uno + dvd + ar
            print (f'AR')
            print (f'DVD')
            print (f'{uno:.1f}')
        if r1 == 'SIM' and r2 == 'SIM' and r3 == 'SIM':
            uno = uno + dvd + ar + som
            print (f'SOM')
            print (f'AR')
            print (f'DVD')
            print (f'{uno:.1f}')
        if r1 == 'SIM' and r2 == 'SIM' and r3 == 'NAO':
            uno = uno + ar + som
            print (f'SOM')
            print (f'AR')
            print (f'{uno:.1f}')
        if r1 == 'SIM' and r2 == 'NAO' and r3 == 'SIM':
            uno = uno + dvd + som
            print (f'SOM')
            print (f'DVD')
            print (f'{uno:.1f}')

    if car == 'PALIO':
        if r1 == 'NAO' and r2 == 'NAO' and r3 == 'SIM':
            palio = palio + dvd
            print (f'DVD')
            print (f'{palio:.1f}')
        if r1 == 'NAO' and r2 == 'SIM' and r3 == 'NAO':
            palio = palio + ar
            print (f'AR')
            print (f'{palio:.1f}')
        if r1 == 'SIM' and r2 == 'NAO' and r3 == 'NAO':
            palio = palio + som
            print (f'SOM')
            print (f'{palio:.1f}')
        if r1 == 'NAO' and r2 == 'SIM' and r3 == 'SIM':
            palio = palio + dvd + ar
            print (f'AR')
            print (f'DVD')
            print (f'{palio:.1f}')
        if r1 == 'SIM' and r2 == 'SIM' and r3 == 'SIM':
            palio = palio + dvd + ar + som
            print (f'SOM')
            print (f'AR')
            print (f'DVD')
            print (f'{palio:.1f}')
        if r1 == 'SIM' and r2 == 'SIM' and r3 == 'NAO':
            palio = palio + ar + som
            print (f'SOM')
            print (f'AR')
            print (f'{palio:.1f}')
        if r1 == 'SIM' and r2 == 'NAO' and r3 == 'SIM':
            palio = palio + dvd + som
            print (f'SOM')
            print (f'DVD')
            print (f'{palio:.1f}')

    if car == 'FIORINO':
        if r1 == 'NAO' and r2 == 'NAO' and r3 == 'SIM':
            fiorino = fiorino + dvd
            print (f'DVD')
            print (f'{fiorino:.1f}')
        if r1 == 'NAO' and r2 == 'SIM' and r3 == 'NAO':
            fiorino = fiorino + ar
            print (f'AR')
            print (f'{fiorino:.1f}')
        if r1 == 'SIM' and r2 == 'NAO' and r3 == 'NAO':
            fiorino = fiorino + som
            print (f'SOM')
            print (f'{fiorino:.1f}')
        if r1 == 'NAO' and r2 == 'SIM' and r3 == 'SIM':
            fiorino = fiorino + dvd + ar
            print (f'AR')
            print (f'DVD')
            print (f'{fiorino:.1f}')
        if r1 == 'SIM' and r2 == 'SIM' and r3 == 'SIM':
            fiorino = fiorino + dvd + ar + som
            print (f'SOM')
            print (f'AR')
            print (f'DVD')
            print (f'{fiorino:.1f}')
        if r1 == 'SIM' and r2 == 'SIM' and r3 == 'NAO':
            fiorino = fiorino + ar + som
            print (f'SOM')
            print (f'AR')
            print (f'{fiorino:.1f}')
        if r1 == 'SIM' and r2 == 'NAO' and r3 == 'SIM':
            fiorino = fiorino + dvd + som
            print (f'SOM')
            print (f'DVD')
            print (f'{fiorino:.1f}')
principal()