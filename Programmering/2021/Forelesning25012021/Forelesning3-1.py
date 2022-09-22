# Program for å boblesortere en usortert liste
# Program forelesning 25012021-2 med forkorta kommentarer

usortert = [7,6,5,4,3,2,1]

bytte = True
tabellengde = len(usortert)
j = 1

print('Tabell før sortering       ',usortert)
print()
print()

print('Start på WHILE-løkka')
while bytte:
    print('Gjennomgang starter')
    bytte = False
    print('Start på FOR-løkka')
    for indeks in range(0,tabellengde-j,1):
        if usortert[indeks] > usortert[indeks + 1]:
            # Da må det byttes
            bytte = True
            x = usortert[indeks]
            usortert[indeks] = usortert[indeks + 1]
            usortert[indeks + 1] = x
            print('Tabell etter hvert bytte innen en gjennomgang',usortert)
        # Slutt på if-testen
    # Slutt på FOR-løkka
    print('Slutt på FOR-løkka')
    print()

    # Teller for å holde orden på sammenligningsslutt i tabellen økes med 1
    j = j+1
print('Slutt på WHILE-løkka')

print()
print('Sortert tabell',usortert)
