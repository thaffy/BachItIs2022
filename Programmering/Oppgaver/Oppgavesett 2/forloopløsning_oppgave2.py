# Lag et program som tar imot 5 tall som inndata, og som skriver ut verdien og "tallnr" på det minste tallet.
# Programmet skal bruke løkker.

fortsette = True
while fortsette == True:

    for i in range(1,6,1):
        verdi = float(input('Skriv et tall: '))
        if i == 1:
            minstetall = verdi
            tallnr = i
        else:
            if verdi < minstetall:
                minstetall = verdi
                tallnr = i

        
    print('----')
    print('Det minste tallet er',minstetall,'og det var nr',tallnr,' i rekka.')
