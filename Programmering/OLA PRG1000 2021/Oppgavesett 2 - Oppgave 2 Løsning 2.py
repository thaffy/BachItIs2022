
verdi = float(input('Skriv et tall: '))
minstetall = verdi
tallnr = 1

for i in range(1,5,1):
    verdi = float(input('Skriv et tall: '))

    if verdi < minstetall:
        minstetall = verdi
        tallnr = tallnr + 1

print('Det minste tallet er:',minstetall,'og det var nr',tallnr,'i rekka.')
print()
        
        

    
