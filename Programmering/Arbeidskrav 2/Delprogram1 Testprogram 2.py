
def leggtilstudent():
    # Delprogram for å legge til nye studenter i student.txt
    print('------------------------------')
    print('Valg 1 - Legg til student.')
    print('-')

    leggtilstudent_fortsette = True
    
    while leggtilstudent_fortsette == True:
        
        # Bolsk variabel som brukes til duplikat-sjekk
        duplikat = False

        studentnr_input=input('Skriv inn studentnummer: ')

        student_fil=open('student.txt','r')

        # Leser første linje
        studnr = student_fil.readline()

        while studnr != '':
            # Leser andre, tredje og fjerde linje
            fornavn = student_fil.readline()
            etternavn = student_fil.readline()
            studerer = student_fil.readline()

            # Fjerner linjeskift \n
            studnr = studnr.rstrip('\n')
            fornavn = fornavn.rstrip('\n')
            etternavn = etternavn.rstrip('\n')
            studerer = studerer.rstrip('\n')

            if studentnr_input == studnr:
                duplikat = True
                
            studnr=student_fil.readline()

        if duplikat == True:
            print('------------------------------')
            print('Du oppga studentnummer',studentnr_input,'.')
            print('Denne studenten eksisterer allerede i systemet.')
            print('------------------------------')
            student_fil.close()
        else:
            # Lukker student.txt som var i read-modus.
            student_fil.close()

            # Åpner student.txt i append modus.
            student_fil = open('student.txt','a')

            # Spør om resten av informasjonen om studenten først etter at duplikat-sjekk er gjort
            fornavn_input = input('Skriv inn fornavn: ')
            etternavn_input = input('Skriv inn etternavn: ')
            studie_input = input('Skriv inn studie: ')

            # Legger til input fra bruker i student.txt
            student_fil.write(studentnr_input + '\n')
            student_fil.write(fornavn_input + '\n')
            student_fil.write(etternavn_input + '\n')
            student_fil.write(studie_input + '\n')
            

        student_fil.close()
        
        # Spør om bruker vil legge til flere studenter.
        svar = input('Vil du legge til en ny student? j/n: ')
        
        if svar == 'n' or svar == 'N' or svar == 'nei' or svar == 'Nei' or svar == 'NEI':
            leggtilstudent_fortsette = False




