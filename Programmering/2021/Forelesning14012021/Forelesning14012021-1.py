def beregn_gjennomsnitt():
    summen = 0
    antall = 0

    tall_fil = open('Tall.txt','r')

    tallnr = tall_fil.readline()

    while tallnr != '':
        tall = int(tall_fil.readline())

        summen = summen + tall
        antall = antall + 1

        tallnr = tallnr.rstrip('\n')
        print(tallnr,'er',tall)

        tallnr = tall_fil.readline()

    tall_fil.close()

    print()
    print('Summen av tallene er:',summen)
    print('Det er',antall,'tall.')

    gjennomsnitt=format((summen/antall),'.2f')
    print('Gjennomsnittet av tallene er:',gjennomsnitt)

    

beregn_gjennomsnitt()
