
# Variabel som bestemmer om programmet skal kjøres på nytt eller ikke

program_restart='Ja'
while program_restart:
    bilpris=int(input('Hva koster bilen du skal kjøpe? '))
    egenkapital=int(input('Hvor mye har du i egenkapital? '))
    antall_ar=int(input('Hvor mange år vil du bruke på nedbetaling av lånet? '))

    egenkapital_prosent=(egenkapital/bilpris)*100

    # Utregning av % av brukerens egenkapital i forhold til bilens pris.
    # Finner også ut av hvilken årlig rente brukeren skal tildeles basert på hvor mye egenkapital brukeren har.
    if egenkapital_prosent<35:
        print('Du har ikke oppfylt kravet om minimum 35% egenkapital.' )
    else:
        if egenkapital_prosent>=35 and egenkapital_prosent<50:
            arlig_rente=4.5
        else:
            if egenkapital_prosent>=50 and egenkapital_prosent<60:
                arlig_rente=3
            else:
                arlig_rente=2.5

    # Utregning av lånesum, terminer og terminrente
    lanesum=bilpris-egenkapital
    antall_terminer=antall_ar*12
    termin_rente=(arlig_rente/12)/100

    # Utregning av terminbeløp
    termin_belop=lanesum*((1+termin_rente)**antall_terminer)*termin_rente/(((1+termin_rente)**antall_terminer)-1)

    print('Antall terminer blir da',antall_terminer)
    print('Din årlige rente blir da',arlig_rente)
    print('Din termin rente blir da',termin_rente)
    print('Terminbeløpet blir da',termin_belop)

    program_slutt=input('Vil du kjøre programmet på nytt? (Ja/Nei) ')
    if program_slutt=='Nei':
        program_restart=False
    else:
        program_restart=True
    
        
    
    

    
    
    
        
