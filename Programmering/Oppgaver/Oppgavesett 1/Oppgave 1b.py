# Oppgave 1 b)
# Dersom det er 10 deltakere eller flere er tillegget pr deltaker 380 kr.
# Lag et program som beregner og skriver ut total pris basert på antall deltakere som inndata.

# Spør om antall deltakere
antall_deltakere=int(input('Hvor mange deltakere er det? '))

# Justerer pris basert på antall deltakere
if antall_deltakere>9:
    pris_per_person=380
else:
    pris_per_person=420

# Beregner totalpris
baneleie=2500
total_leie=baneleie+antall_deltakere*pris_per_person

# Skriver ut totalsum
print()
print('Med',antall_deltakere,'deltakere blir leien per person',pris_per_person)
print('Den totale leien av paintballbanen blir',total_leie,'kr.')

