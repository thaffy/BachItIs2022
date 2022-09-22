def les_fra_fil_til_liste():
    # Oppretter lista
    tall_liste = []
    
    try:
        # Åpner tall-fila for lesing
        tall_fil = open('tallmedbokstav.txt','r')

        # Leser hele fila linje for linje med while-løkke og test på eof, s336
        # Leser første linje før løkka starter
        # Vente med å konvertere til heltall til etter sjekk på EOF
        tall = tall_fil.readline()

        while tall != '':
            # Konvertere
            tall = int(tall)
            # Legger tallet inn i lista
            tall_liste += [tall]
            # Leser neste tall i fila
            tall = tall_fil.readline()

        # Lukker fila
        tall_fil.close()

    except IOError:
        # Sikrer oss at fila eksistere, og feilmelding hvis ikke funnet
        print('Det oppsted en feil ved lesing av fila med tall')

    except ValueError:
        # Sikrer oss at fila har gyldige data, og feilmelding hvis ugyldige verdier
        print('Datafila inneholder verdier som ikke er tall')

    else:
        # Ingen feil funnet
        print('Ingen feil i datafil og tallene er lest inn i lista')
        print('Resultatet ble:',tall_liste)
            
        

    


les_fra_fil_til_liste()
