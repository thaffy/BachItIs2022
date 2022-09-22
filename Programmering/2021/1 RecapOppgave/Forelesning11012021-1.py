def read_metode():
    print('-----')
    print('- Valg 1 - Les hele fila med read-metoden og skriver ut')
    print('-----')

    tall_fil = open('Tall.txt','r')
    les_fil = tall_fil.read()
    
    tall_fil.close()

    print(les_fil)
    print()


def forloop_metode():
    print('-----')
    print('- Valg 2 - Les hele fila med for-løkke og skriver ut')

    tall_fil = open('Tall.txt','r')

    for line in tall_fil:
        line = line.rstrip('\n')
        print(line)
        
    tall_fil.close()
    print()


def linjeforlinje_metode():
    print('-----')
    print('- Valg 3 - Les hele fila linje for linje og skriver ut')

    tall_fil = open('Tall.txt','r')

    tallnr = tall_fil.readline()

    while tallnr != '':
        tall = tall_fil.readline()

        tallnr = tallnr.rstrip('\n')
        tall = tall.rstrip('\n')

        print(tallnr)
        print(tall)

        tallnr = tall_fil.readline()
        
    tall_fil.close()
    print()


def summering():
    print('- Valg 4 - Les hele fila linje for linje og summerer tallene')
    total_sum = 0

    tall_fil = open('Tall.txt','r')

    tallnr = tall_fil.readline()

    while tallnr != '':
        tall = tall_fil.readline()

        tallnr = tallnr.rstrip('\n')
        tall = tall.rstrip('\n')

        total_sum = total_sum + int(tall)



        tallnr = tall_fil.readline()
        
    tall_fil.close()
    
    print('- Summen av alle tallene i filen er:',total_sum)
    print()


def gjennomsnitt():
    print(' Valg 5 - Les hele fila linje for linje og beregner gjennomsnitt')
    total_sum = 0
    antall_tall = 0

    tall_fil = open('Tall.txt','r')

    tallnr = tall_fil.readline()

    while tallnr != '':
        tall = tall_fil.readline()

        tallnr = tallnr.rstrip('\n')
        tall = tall.rstrip('\n')

        antall_tall = antall_tall + 1
        total_sum = total_sum + int(tall)



        tallnr = tall_fil.readline()
        
    tall_fil.close()
    gjennsomsnittet = total_sum / antall_tall
    
    print('Antall tall er:',antall_tall)
    print('Totalsum er: ',total_sum)
    print('Gjennomsnittet av tallene blir da:',gjennsomsnittet)
    print()

def storste_tall():
    print('- Valg 6 - Les hele fila linje for linje og finn største tall med tallnr')

    stort_tall = 0
    korrekt_tallnummer = 1
    tall_fil = open('Tall.txt','r')

    tallnr = tall_fil.readline()

    while tallnr != '':
        tall = tall_fil.readline()

        tallnr = tallnr.rstrip('\n')
        tall = tall.rstrip('\n')

        if int(tall) > int(stort_tall):
            stort_tall = tall
            korrekt_tallnummer = tallnr
        else:
            stort_tall = stort_tall
            korrekt_tallnummer = korrekt_tallnummer

        tallnr = tall_fil.readline()

    print('Det største tallet er',stort_tall,'som er',korrekt_tallnummer,'i filen.')
    print()


def main():

    fortsette = True
    
    while fortsette == True:
    
        # Koden for menyen som starter programmet og sender bruker til de forskjellige delprogrammene.
        print('-----')
        print('- Hovedmeny')
        print('- Valg 1: Les hele fila med read-metoden og skriver ut.')
        print('- Valg 2: Les hele fila med for-løkke og skriver ut.')
        print('- Valg 3: Les hele linja linje for linje og skriver ut.')
        print('-')
        print('- Valg 4: Leser fila og summerer tallene')
        print('- Valg 5: Leser fila og beregner gjennomsnitt av tallene')
        print('- Valg 6: Leser fila og finner største tall med tilhørende tallnr.')
        print('-----')
        programvalg=int(input('Hva vil du gjøre? '))

        if programvalg == 1:
            read_metode()
        else:
            if programvalg == 2:
                forloop_metode()
            else:
                if programvalg == 3:
                    linjeforlinje_metode()
                else:
                    if programvalg == 4:
                        summering()
                    else:
                        if programvalg == 5:
                            gjennomsnitt()
                        else:
                            if programvalg == 6:
                                storste_tall()
                            else:
                                print('Programmet er avsluttet!')
                                fortsette = False

main()
