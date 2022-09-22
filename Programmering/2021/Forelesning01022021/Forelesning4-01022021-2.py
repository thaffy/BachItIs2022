# Oppretter en tom liste
ansatte = []
print(ansatte)

ansattfil = open('laerer.txt','r',encoding='utf-8')

fornavn = ansattfil.readline()

while fornavn != '':
    fornavn = fornavn.rstrip('\n')
    
    etternavn = ansattfil.readline().rstrip('\n')
    epost = ansattfil.readline().rstrip('\n')

    # Legger posten inn i lista, "liste i liste"-tankegang
    ansatte += [[fornavn,etternavn,epost]]

    fornavn = ansattfil.readline()

# Lukker fila
ansattfil.close()

print('Resultatet ble:',ansatte)

# Skriver ut hele lista
print(ansatte)
print()
# Skriver ut en post, aka all info om én ansatt
print(ansatte[4])
print()
# Skriver ut én verdi
print(ansatte[4][2])
