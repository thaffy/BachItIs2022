# Lag et program som tar imot 5 tall som inndata, og som skriver ut verdien og "tallnr" på det minste tallet.


# Får inn 5 tallverdier.
verdi1=float(input('Skriv inn tall nr 1: '))
verdi2=float(input('Skriv inn tall nr 2: '))
verdi3=float(input('Skriv inn tall nr 3: '))
verdi4=float(input('Skriv inn tall nr 4: '))
verdi5=float(input('Skriv inn tall nr 5: '))

if verdi1<verdi2:
    minste_tall=verdi1
    tallnr=1
else:
    minste_tall=verdi2
    tallnr=2

if minste_tall<verdi3:
    minste_tall=verdi3
    tallnr=3
else:
    minste_tall=minste_tall
    tallnr=tallnr



print('Det minste tallet er',minste_tall)
print('Du skrev inn tallet som nr',tallnr,)


