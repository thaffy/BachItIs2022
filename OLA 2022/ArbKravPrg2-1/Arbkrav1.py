import os

vareliste = []

varefil = open('Varer.txt','r')
varenr = varefil.readline()

while varnr != '':
    betegnelse = varefil.readline()
    pris = varefil.readline()
    kategori = varefil.readline()
    hylle = varefil.readline()

    varenr = varenr.rstrip('\n')
    betegnelse = betegnelse.rstrip('\n')
    pris = pris.rstrip('\n')
    kategori = kategori.rstrip('\n')
    hylle = hylle.rstrip('\n')
    
    vareliste += [varenr,betegnelse,pris,kategori,hylle]

    varenr = varefil.readline()

varefil.close()
print(vareliste)



