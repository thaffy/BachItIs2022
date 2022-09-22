# Oppretter en tom liste

vare = []
print(vare)

varefil = open('Varer.txt','r',encoding='utf-8')

vnr = varefil.readline()

while vnr != '':
    vnr = vnr.rstrip('\n')

    betegnelse = varefil.readline().rstrip('\n')
    kategori = varefil.readline().rstrip('\n')
    hylle = varefil.readline().rstrip('\n')

    vare += [[vnr,betegnelse,kategori,hylle]]

    vnr = varefil.readline()

varefil.close()

print('Resultatet ble:',vare)
print()

# Teller poster i tabellen, hvis den er todimensjonal (liste i liste, eller [->[]<-]
antall_poster = len(vare)
print('Antall rader/poster er',antall_poster)
print()

# Skriver ut alle varer
print('Varer:')
c = 1
for r in range (antall_poster):
    print(vare[r][c])
print()

# Skriver ut alle varer med hylleplassering
print('Varer og hylleplass')
c=1
for r in range(antall_poster):
    print(vare[r][c],'har hylleplass',vare[r][c+2])
print()

# Skriver ut alle varer og hylleseksjon, tar ikke med varer som ikke er hylleplasserte
# slicing - > [0:1] velger bare første tegn i verdien. [0:2] ville valgt de 2 første tegnene.
print('Varer og hylleseksjon')
c = 1
for r in range(antall_poster):
    if vare[r][c+2] != 'NULL':
        print(vare[r][c],'hører til hylleseksjon',vare[r][c+2][0:1])
print()

# Skriver ut alle varr og hylleseksjon, tar ikke med varer som ikke er hylleplasserte
# slicingen gjøres på en variabel
print('Varer og hylleseksjon')
c = 1
for r in range(antall_poster):
    if vare[r][c+2] != 'NULL':
        hylle = vare[r][c+2]
        print(vare[r][c],'hører til hylleseksjon',hylle[0:1])
print()

# Test på innhold i en streng
# Varer i kategori for blomster, jfr DAT1000

c = 2
print('Blomstervarer')
for r in range(antall_poster):
    if "BLOMST" in vare[r][c].upper():
        print(vare[r][c-1],'i kategorien',vare[r][c])
print()

# sett i forhold til uten konvertering til uppercase (får ingen resultat da kategoriene er skrevet med stor forbokstav)
c = 2
print('Blomstervarer')
for r in range(antall_poster):
    if "blomst" in vare[r][c]:
        print(vare[r][c-1],'i kategorien',vare[r][c])
print()

# Generalisert, søkekriteret som inndata
sokekriterie = input('Oppgi varetype det skal søkes på: ')
c = 2
for r in range(antall_poster):
    if sokekriterie.upper() in vare[r][c].upper():
        print(vare[r][c-1],'i kategorien',vare[r][c].lower())


















    
