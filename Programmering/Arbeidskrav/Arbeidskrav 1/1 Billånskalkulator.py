
#Billåns kalkulator

program_restart='Ja'

while program_restart:
    
    bilpris=int(input('Hva koster bilen du skal kjøpe? '))
    bruker_egenkapital=int(input('Hvor mye har du i egen kapital? '))
    antall_ar=int(input('Hvor mange år vil du bruke på nedbetaling av lånet? '))

    egenkapital_prosent=(bruker_egenkapital/bilpris)*100
    lanesum=bilpris-bruker_egenkapital


    if egenkapital_prosent<35:
        print()
        print('Din egenkapital i forhold til bilens prins er',egenkapital_prosent,'%.')
        print('Du har ikke oppfylt kravet om minimum 35% egenkapital.')
    else:
        if egenkapital_prosent>=60:
             arlig_rente=2.5
        else:
            if egenkapital_prosent>=50.60:
                arlig_rente=3
            else:
                if egenkapital_prosent>=35:
                    arlig_rente=4.5

    antall_terminer=antall_ar*12
    termin_rente=(arlig_rente/12)/100

    termin_belop=lanesum*((1+termin_rente)**antall_terminer)*termin_rente/(((1+termin_rente)**antall_terminer)-1)

    print('Antall terminer blir da',antall_terminer)
    print('Din årlige rente blir da',arlig_rente)
    print('Din termin rente blir da',termin_rente)
    print('Terminbeløpet blir da',termin_belop)

    program_slutt=input('Vil du kjøre programmet på nytt?' )
    


                
        



