minstetall = 1000000

for i in range(1,6,1):
    verdi=float(input('Skriv et tall: '))

    if verdi < minstetall:
        minstetall = verdi
        tallnr = i

print('Minste tall er:',minstetall,'og det var nr',tallnr,'i rekka.')
print()
        

    
