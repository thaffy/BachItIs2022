kolonner = 3

# Antall rader/poster må beregnes

# Leser og teller linjer i én operasjon.
ansattfil = open('laerer.txt','r',encoding='utf-8')
antall_linjer = sum(1 for line in ansattfil)
ansattfil.close()
print('Antallet linjer på fila er',antall_linjer)
rader = antall_linjer//kolonner
print('Det gir',rader,'rader i tabellen, én rad er én post')

# Oppretter tabellen
# Den innerste (kolonner) for hver rad, legger inn en "tom streng" for hver verdi
ansatte = [['' for c in range(kolonner)] for r in range(rader)]
print(ansatte)

ansattfil = open('laerer.txt','r',encoding='utf-8')

# Når vi skal dataene inn i tabellen må vi starte med rad-løkka før kolonne-løkka
# jfr henvisning til en verdi ved (radindeks,kolonneindeks) [r][c]
for r in range(rader):
    for c in range(kolonner):
        # Leser linje fra fil og legger inn i tabellelement i én operasjon
        ansatte[r][c] = ansattfil.readline().rstrip('\n')

ansattfil.close()

print()
print('Resultatet ble:',ansatte)
print()

# Skriver ut hele tabellen
print(ansatte)
print()

# Skriver ut en post
print(ansatte[4])
print()

# Skriver ut en verdi
print(ansatte[4][2])
print()

# Skrive ut alle etternavn
print('Etternavn:')
c = 1
for r in range(rader):
    print(ansatte[r][c])
print()

# Skrive ut alle etternavn og epostadresser

print('Etternavn og epost adresser:')
c = 1
for r in range(rader):
    print(ansatte[r][c],'-',ansatte[r][c+1])
    
