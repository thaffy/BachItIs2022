# Billånskalkulator

# program_start avgjør om programmet skal kjøres på nytt eller ikke. 
program_start='Ja'

# While-løkke for restart av programmet.
while program_start=='Ja':

    # Spør om bilpris og egenkapital fra bruker, som gjør det mulig å beregne andel egenkapital i %.
    bilpris=int(input('Hva koster bilen du skal kjøpe? '))
    egenkapital=int(input('Hvor mye har du i egenkapital? '))
    

    # Regner ut forholdet mellom egenkapital og bilens kjøpesum.
    egenkapital_prosent=(egenkapital/bilpris)*100

    # if-test for å determinere om bruker har oppfylt kravet om 35% egenkapital.
    if egenkapital_prosent<35:
        print()
        print('Du har ikke oppfylt kravet om minimum 35% egenkapital.')
    else:
        # Videre if-test for å determinere årlig rente basert på % egenkapital.
        if egenkapital_prosent>=35 and egenkapital_prosent<50:
            arlig_rente=4.5
        else:
            if egenkapital_prosent>=50 and egenkapital_prosent<60:
                arlig_rente=3
            # Siden alle egenkapital %-intervaller fra 0-60 er gjort rede før så vil egenkapital % over 60% bli 2.5
            else:
                arlig_rente=2.5

        # Spør om hvor mange år lånet skal betales ned på, etter at kravet om egenkapital er oppfylt. 
        antall_ar=int(input('Hvor mange år vil du bruke på nedbetaling av lånet? '))

        # Utregning av lånesum, antall terminer og terminrente
        lanesum=bilpris-egenkapital
        antall_terminer=antall_ar*12

        # Siden jeg har beholdt rente-tallet som '4.5, 3 og 2.5' så har jeg delt (arlig_rente/12) på 100 for å få riktig terminrente for formelen.
        termin_rente=(arlig_rente/12)/100
        
        # Utregning av terminbeløpet etter oppgitt formel
        termin_belop=lanesum*((1+termin_rente)**antall_terminer)*termin_rente/(((1+termin_rente)**antall_terminer)-1)

        # Skriver ut informasjon til brukeren om lånesum, årlig rente, antall terminer og terminbeløpet.
        # Bruker kan verifisere basert på utdataen om inndataen var korrekt.
        print()
        print('Du vil låne',lanesum,'kr.')
        print('Den årlige renten blir satt til',arlig_rente,'%.')
        print('Antall terminer på lånet blir',antall_terminer,)
        print('Terminbeløpet blir',format(termin_belop, '.2f'),'kr.')
        
    # Spør bruker om programmet skal kjøres på nytt.
    program_start=input('Vil du kjøre programmet på nytt? (Ja/Nei) ')

        
    
        
        



        
    
       
