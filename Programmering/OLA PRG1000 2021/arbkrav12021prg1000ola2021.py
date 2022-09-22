fortsett = True
while fortsett:
    kjopeSum = int(input('Hvor mye vil du låne? '))
    egenkapital = int(input('Hvor mye har du i egenkapital? '))
    bruttoinntekt = int(input('Hvor mye har husstanden i inntekt? '))
    
    print()
    
    egenkapitalProsent = egenkapital / kjopeSum
    inntektsKrav = bruttoinntekt * 5
    laneSum = kjopeSum - egenkapital
    
    if egenkapitalProsent < 0.15:
        print('Du har ikke nok egenkapital til å få lån.')
    else:
        if laneSum <= inntektsKrav:
            print('Lån innvilges!')
            print('Du får',laneSum,'kr innvilget for dette boliglånet.')
        else:
            print('Husholdningens samlede inntekt er for liten.')
            
    print()
    
    svar = input('Vil du kjøre programmet på nytt? n/j ')
    if svar == 'Nei' or svar == 'nei' or svar == 'n' or svar == 'N':
        fortsett = False
        print('Program avsluttet!')
