#Oppgave 1a
# En utleier av paintball (bane og utstyr) beregner sine priser på følgende måte:
# Leie av bane: 2.500 kr
# Tillegg pr deltaker: 420 kr
# Lag et program som beregner og skriver ut total pris basert på antall deltakere som inndata.

# Spør om antall deltakere
antall_deltakere=int(input('Hvor mange deltakere er det? '))

# Beregner totalleie

baneleie=2500
total_leie=baneleie+antall_deltakere*420

# Skriver ut totalsum
print()
print('Den totale leien av paintballbanen blir',total_leie,'kr.')


