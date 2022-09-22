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
    # Fornavn som nøkkel på øverste nivå,
    # og etternavn og epost i ny dictionary, og egne key'er
    
    ansatte[fornavn] = {'etternavn':etternavn,'epost':epost}

    fornavn = ansattfil.readline()
    
ansattfil.close()

print('Resultatet ble: ')
print(ansatte)
print()

# Skriver ut info om Gunnar, dvs dictionary'en knyttet til key value 'Gunnar' på øverste nivå
print(ansatte['Gunnar'])
print()

# Skrive ut Gunnars epost, key value 'Gunnar' på øverste nivå, og key value e-post på nivå 2.
print(ansatte['Gunnar']['epost'])
print()

# Skriver ut nøkkel og e-post
for key in ansatte:
    print(key,ansatte[key]['epost'])
print()
