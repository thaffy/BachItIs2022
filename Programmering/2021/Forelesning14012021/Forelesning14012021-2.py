def les_hele_sum():
    summen = 0

    try:
        tall_fil = open('tallmedbokstav.txt','r')

        tall = tall_fil.readline()

        while tall != '':
            tall = int(tall)
            summen = summen + tall

            tall = tall_fil.readline()
            
        tall_fil.close()

    except IOError:
        print('Det oppstod en feil ved lesing av fila med tall')

    except ValueError:
        print('Datafila inneholder verdier som ikke er tall')
        print('Summen av tallene er:',summen)
        print('Tall fram til ValueError er summert opp og skrevet ut over.')

    else:
        print('Ingen feil i datafila, og summen av tallene er:',summen)
                    

les_hele_sum()
