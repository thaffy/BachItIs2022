import os

vareliste = []


varefil = open('Varer.txt','r')
varenr = varefil.readline()

while varenr != '':
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

listelengde = len(vareliste)
index = 2

for i in range(listelengde):

        # Last i elements are already in place
        for j in range(0, listelengde-i-1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if int(vareliste[j][index]) > int(vareliste[j+1][index]) :
                vareliste[j], vareliste[j+1] = vareliste[j+1], vareliste[j]
print()
print(vareliste)




