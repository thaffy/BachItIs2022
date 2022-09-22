def summering():
    try:
        tallliste = open('tallmedbokstav.txt','r')


        total_sum = 0
        tall = tallliste.readline()

        tall_liste = []

        while tall != '':

            tall = tall.rstrip('\n')
            total_sum = int(total_sum) + int(tall)

            tall_liste += [int(tall)]

            tall = tallliste.readline()

        tallliste.close()

        

        

    except IOError:
        print('Feil! - IO Error')
        print('Filen som skulle åpnes kunne ikke finnes...Har du plassert den riktig?')

        
    except ValueError:
        print('Feil! - Value Error')
        print('En av verdiene i talllisten var ugyldig.')
        print('Summen fram til feil ble:',total_sum)
        print('Tallene i liste:',tall_liste)
    else:
        print('Totalsum:',total_sum)
        print('Tallene i liste:',tall_liste)
        
summering()

            
