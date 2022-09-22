# a)
#En utleier av paintball (bane og utstyr) beregner sine priser på følgende måte:
#Leie av bane: 2.500 kr
#Tillegg pr deltaker: 420 kr
#Lag et program som beregner og skriver ut total pris basert på antall deltakere som inndata.

# b)
#Dersom det er 10 deltakere eller flere er tillegget pr deltaker 380 kr.
#Lag et program som beregner og skriver ut total pris basert på antall deltakere som inndata.

# c)
#Dersom det er 20 deltakere eller flere er tillegget pr deltaker 350 kr.
#Lag et program som beregner og skriver ut total pris basert på antall deltakere som inndata.

# Spør om antall deltakere
antall_deltakere=int(input('Hvor mange deltakere er det? '))

if antall_deltakere<10:
    pris_per_person=420
else:
    if antall_deltakere<20:
        pris_per_person=380
    else:
        pris_per_person=350

# Beregner totalpris
baneleie=2500
total_leie=baneleie+antall_deltakere*pris_per_person

# Skriver ut totalsum
print()
print('Med',antall_deltakere,'deltakere blir leien per person',pris_per_person)
print('Den totale leien av paintballbanen blir',total_leie,'kr.')
    
