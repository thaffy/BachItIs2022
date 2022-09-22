# Lag et program som tar imot 5 tall som inndata, og som skriver ut verdien og "tallnr" på det minste tallet.
# Programmet skal bruke løkker.

fortsette = True
while fortsette == True:
    # Får inn 5 tallverdier.

    minste_tall = 1000000*463657275
    tallnr = 1
    for i in range(1,6,1):
        verdi = float(input('Skriv inn et tall: '))

        if verdi<minste_tall:
            minste_tall = verdi
            tallnr = i
        

##    if verdi1<verdi2:
##        minste_tall=verdi1
##        tallnr=1
##    else:
##        minste_tall=verdi2
##        tallnr=2
##        
##    if minste_tall<verdi3:
##        minste_tall=minste_tall
##    else:
##        minste_tall=verdi3
##        tallnr=3
##
##    if minste_tall<verdi4:
##        minste_tall=minste_tall
##    else:
##        minste_tall=verdi4
##        tallnr=4
##
##    if minste_tall<verdi5:
##        minste_tall=minste_tall
##    else:
##        minste_tall=verdi5
##        tallnr=5

    print('Det minste tallet er',minste_tall)
    print('Du skrev inn tallet som nr',tallnr,)
    print()
    svar = input('Vil du kjøre programmet på nytt? ')

    if svar == '1' or svar == 'Ja' or svar == 'ja':
        fortsette = True
    else:
        fortsette = False
        
    print()


