# Billånskalkulator


# Verdi for å avgjøre om programmet skal kjøres på nytt eller ikke
ny_utregning='Ja'

# While-løkke for restart av programmet
while ny_utregning:
    bilpris=int(input('Hva koster bilen du skal kjøpe? '))
    egenkapital=int(input('Hvor mye har du i egenkapital? '))
    antall_ar=int(input('Hvor mange år vil du bruke på nedbetaling av lånet? '))

    egenkapital_prosent=(egenkapital/bilpris)*100

    if egenkapital_prosent<35:
        print('Du har ikke oppfylt kravet om minimum 35% egenkapital.')
    else:
        if egenkapital_prosent>=35 and egenkapital_prosent<50:
            arlig_rente=4.5
        else:
            if egenkapital_prosent>=50 and egenkapital_prosent<60:
                arlig_rente=3
            else:
                arlig_rente=2.5

    lanesum=bilpris-egenkapital
    antall_terminer=antall_ar*12
    termin_rente=(arlig_rente/12)/100

    termin_belop=lanesum*((1+termin_rente)**antall_terminer)*termin_rente/(((1+termin_rente)**antall_terminer)-1)
            
    
