# d)
# Firmaet vurderer å gå over til en ny prisstrategi
# 3.500 kr i baneleie og 350 kr pr deltaker for inntil 9 deltakere
# 2.000 kr i baneleie og 400 kr pr deltaker fra 10 inntil 19 deltakere
# 1.000 kr i baneleie og 450 kr pr deltaker fra 20 deltaker
# Maks kapasitet på en leieavtale er 30 deltakere.
# Lag et program som på bakgrunn av antall deltakere sammenligner og skriver ut pris etter gammel prisstrategi (a)-c)) og ny prisstrategi (d)) og skriver ut hvilken prisstrategi som er best for firmaet for det oppgitte deltakerantallet.

# Spør om antall deltakere
antall_deltakere=int(input('Hvor mange deltakere er det? '))

# Beregner pris etter gammel strategi
if antall_deltakere<10:
    pris_per_person=420
else:
    if antall_deltakere<20:
        pris_per_person=380
    else:
        pris_per_person=350

# Beregner pris etter ny strategi
if antall_deltakere<10:
    ny_pris_per_person=350
    ny_baneleie=3500
else:
    if antall_deltakere<20:
        ny_pris_per_person=400
        ny_baneleie=2000
    else:
        ny_pris_per_person=450
        ny_baneleie=1000

# Beregner totalpris med gammel strategi
baneleie=2500
total_leie=baneleie+antall_deltakere*pris_per_person

# Beregner totalpris med ny strategi
ny_total_leie=antall_deltakere*ny_pris_per_person+ny_baneleie

# Skriver ut pris etter begge strategiene
print()
print('Med',antall_deltakere,'deltakere blir leien lavest per person etter gammel strategi',pris_per_person,'kr.')
print('Baneleien koster',baneleie,'kr.')
print('Den totale leien av paintballbanen blir da',total_leie,'kr.')
print()
print('Med',antall_deltakere,'deltakere blir leien per person etter ny strategi',ny_pris_per_person,'kr.')
print('Baneleien koster',ny_baneleie,'kr.')
print('Den totale leien av paintballbanen blir da',ny_total_leie,'kr.')


# Sammenlinger prisene og skriver ut den minste
if total_leie<ny_total_leie:
    print('Med',antall_deltakere,'deltakere blir leien lavest etter gammel strategi!')
    print('Pris per person blir',pris_per_person,'kr.')
    print('Baneleien koster',baneleie,'kr.')
    print('Den totale leien av paintballbanen blir da',total_leie,'kr.')
else:
    print('Med',antall_deltakere,'deltakere blir leien lavest etter ny strategi!')
    print('Pris per person blir',ny_pris_per_person,'kr.')
    print('Baneleien koster',ny_baneleie,'kr.')
    print('Den totale leien av paintballbanen blir da',ny_total_leie,'kr.')

    

# Skriver ut totalsum
# print()
# print('Med',antall_deltakere,'deltakere blir leien lavest per person etter gammel strategi',pris_per_person,'kr.')
# print('Baneleien koster',baneleie,'kr.')
# print('Den totale leien av paintballbanen blir da',total_leie,'kr.')
# print()
# print('Med',antall_deltakere,'deltakere blir leien per person etter ny strategi',ny_pris_per_person,'kr.')
# print('Baneleien koster',ny_baneleie,'kr.')
#print('Den totale leien av paintballbanen blir da',ny_total_leie,'kr.')

    
