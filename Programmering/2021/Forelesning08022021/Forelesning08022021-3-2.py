# Oppretter en tom Dictionary
ansatte = {}
print(ansatte)
print()

ansattfil = open('Laerer.txt','r',encoding='utf-8')

fornavn = ansattfil.readline()

while fornavn != '':
    fornavn = fornavn.rstrip('\n')

    etternavn = ansattfil.readline().rstrip('\n')
    epost = ansattfil.readline().rstrip('\n')

    # Legger posten inn i Ditionary'en
    ansatte[fornavn] = [etternavn,epost]

    fornavn = ansattfil.readline()
    
ansattfil.close()

print('Resultatet ble: ')
print(ansatte)
print()

# Skriver ut alle nøkler og deler av opplysningene, nøkkel og e-post

for key in ansatte:
    print(key,ansatte[key][1])
print()

# Skriver ut kun epost-adressene
for key in ansatte:
    print(ansatte[key][1])
print()
