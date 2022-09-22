# Oppretter Dictionary'en
kontakter = {'Kari':11111111,'Knut':22222222,'Lise':33333333,'Lars':44444444}

print('Kontaktlista mi er:',kontakter)
print()

# for å hente ut en verdi fra dictionary'en oppgir du nøkkelen
# !NB! case-sensitiv
print(kontakter['Lise'])
print()

# Dersom nøkkel ikke finnes termineres programmet
# print(kontakter['Tore'])
# Det kan vi løse ved å teste om kontakten finnes vha in-operatoren
if 'Tore' in kontakter:
    print(kontakter['Tore'])

else:
    print('Kontakten "Tore" eksisterer ikke.')
print()

# Søkekritere som inndata
navn = input('Oppgi navn på kontakten: ')
if navn in kontakter:
    print(navn,'har telefonnummeret:',kontakter[navn])
else:
    print('Kontakten',navn,'finnes ikke.')
print()

# Utskrift av alle nøkler med verdier i en for-løkke
for key in kontakter:
    print(key,kontakter[key])
print()

# Legge til kontakt
navn = input('Oppgi navn til ny kontakt: ')
tlfnr = int(input('Oppgi telefonnummer: '))
kontakter[navn] = tlfnr
print(kontakter)
print()
# dersom key-value finnes fra før vil dette bli en overskrivning - ny kontakt m/tlfnr i dette tilfellet

# Slette kontakt
navn = input('Oppgi navn på kontakten som skal slettes: ')
if navn in kontakter:
    print(navn,'har telefonnr',kontakter[navn])
    del kontakter[navn]
else:
    print('Kontakten finnes ikke.')
print(kontakter)
print()
