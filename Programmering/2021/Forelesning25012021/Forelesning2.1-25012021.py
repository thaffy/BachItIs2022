# Program for å boblesortere en usortert liste

usortert = [7,6,5,4,3,2,1]

bytte = True
tabellengde = len(usortert)
j = 1

print('Tabell før sortering       ',usortert)
print()
print()

while bytte:
    bytte = False
    print('Gjennomgang starter, men bare hvis det må byttes, dvs bytte = True')
    print('Gjennomgang nr',j,'starter.')
    for indeks in range(0,tabellengde-j,1):
        print('Sammenligning nr',indeks + 1,'utføres')
        if usortert[indeks] > usortert[indeks + 1]:
            # Da må det byttes
            bytte = True
            x = usortert[indeks]
            usortert[indeks] = usortert[indeks + 1]
            usortert[indeks + 1] = x
            print('Resultat etter bytte nr',indeks+1,':',usortert)
        # Slutt på if-testen
    # Slutt på FOR-løkka
    print()

    # Teller for å holde orden på sammenligningsslutt i tabellen økes med 1
    j = j+1

print()
print('Sortert tabell',usortert)
