# Oppgave 3


fortsette = True

while fortsette == True:

    hund = []
    hund_fil = open('hund.txt','r')


    # Leser første linje i hund.txt
    hunde_id = hund_fil.readline()

    gyldig_oppdretter = False

    while hunde_id != '':
        # leser linje 2 til og med 6
        oppdretter_id = hund_fil.readline()
        hunde_eier_id = hund_fil.readline()
        hund_navn = hund_fil.readline()
        hund_kjonn = hund_fil.readline()
        hund_fodt = hund_fil.readline()

        # Fjerner linjeskift
        hunde_id = hunde_id.rstrip('\n')
        oppdretter_id = oppdretter_id.rstrip('\n')
        hunde_eier_id = hunde_eier_id.rstrip('\n')
        hund_navn = hund_navn.rstrip('\n')
        hund_kjonn = hund_kjonn.rstrip('\n')
        hund_fodt = hund_fodt.rstrip('\n')


            
        hund += [hunde_id,oppdretter_id,hunde_eier_id,hund_navn,hund_kjonn,hund_fodt]


        hunde_id = hund_fil.readline()


    hund_fil.close()
    input_oppdretter_id = input('Oppgi oppdretterID: ')

    
    liste_lengde=len(hund)
    oppdretter_liste = []

    for n in range(0,liste_lengde,1):
        if input_oppdretter_id == hund[n]:
            oppdretter_liste += [hund[n-1],hund[n+1],hund[n+2],hund[n+3]]

    print('Dette er hundene fra denne oppdretteren:')
    print(oppdretter_liste)
    




    svar = input('Vil du kjøre programmet på nytt? ')

    if svar == 'nei' or svar == 'n' or svar =='Nei' or svar =='NEI' or svar =='N':
        fortsette = False
        print('Program avsluttet!')




        
