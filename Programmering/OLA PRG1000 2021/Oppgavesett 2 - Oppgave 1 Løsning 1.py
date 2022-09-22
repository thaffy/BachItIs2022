for i in range(0,550,50):
    pris1 = 750
    pris2 = 350 + (2*i)
    pris3 = 150 + (4*i)

    print('Antall km kjørt:',i,'km.')
    print('Alternativ 1 koster:',pris1)
    print('Alternativ 2 koster:',pris2)
    print('Alternativ 3 koster:',pris3)
    print('---')
    if pris1<pris2:
        print('Alternativ 1 blir det beste for deg. Da blir prisen',pris1,'kr.')
    else:
        if pris2<pris3:
            print('Alternativ 2 er det beste for deg. Da blir prisen',pris2,'kr.')
        else:
            print('Alternativ 3 er det beste for deg. Da blir prisen',pris3,'kr.')
    print('---')
    print()
