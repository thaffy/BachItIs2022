# Billånskalkulator

# program_start avgjør om programmet skal kjøres på nytt eller ikke.
program_start='Ja'

# While-løkke for restart av programmet.
while program_start=='Ja':

    # Spør om input fra brukeren
    bilpris=int(input('Hva koster bilen du skal kjøpe? '))
    egenkapital=int(input('Hvor mye har du i egenkapital? '))
    antall_ar=int(input('Hvor mange år vil du bruke på nedbetaling av lånet? '))

    # Regner ut forholdet mellom egenkapital og bilens kjøpesum.
    egenkapital_prosent=(egenkapital/bilpris)*100

    if egenkapital_prosent<35:
        print()
        print('Du har ikke oppfylt kravet om minimum 35% egenkapital.')
    else:
        if egenkapital_prosent>=35 and egenkapital_prosent<50:
            arlig_rente=4.5
        else:
            if egenkapital_prosent>=50 and egenkapital_prosent<60:
                arlig_rente=3
            else:
                arlig_rente=2.5

        # Utregning av lånesum, antall terminer og terminrente
        lanesum=bilpris-egenkapital
        antall_terminer=antall_ar*12
        termin_rente=(arlig_rente/12)/100

        # Utregning av terminbeløpet
        termin_belop=lanesum*((1+termin_rente)**antall_terminer)*termin_rente/(((1+termin_rente)**antall_terminer)-1)
        print()
        print('Du vil låne',lanesum,'kr.')
        print('Den årlige renten blir satt til',arlig_rente,'%.')
        print('Antall terminer på lånet blir',antall_terminer,'kr')
        print('Terminbeløpet blir',format(termin_belop, '.2f'))
        
    # Spør bruker om programmet skal kjøres på nytt
    program_start=input('Vil du kjøre programmet på nytt? (Ja/Nei) ')
    
        
        



        
    
       
