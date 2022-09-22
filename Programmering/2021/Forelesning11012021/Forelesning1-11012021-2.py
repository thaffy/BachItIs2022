def studenter():
    try:
        studentfil = open('studentoblig99.txt','r')

        # Skrive ut alle studenter
        # Eksemplifisert med enkel innlesning og utskrift av innholdet på studentfila

        alle_studenter = studentfil.read()
        print(alle_studenter)

        studentfil.close()
    except IOError:
        print('Det oppstod en feil ved lesning av studentfila')
        
studenter()

