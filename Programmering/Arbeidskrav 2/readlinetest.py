

duplikat = False

studnr = input('Skriv inn studentnr: ')

student_fil = open('student.txt','r')

les_linje = student_fil.readline()

while les_linje != '':
    fornavn = student_fil.readline()

    les_linje = les_linje.rstrip('\n')

    if les_linje == studnr:
        duplikat = True

        
    les_linje = student_fil.readline()

if duplikat == True:
    print('------------------------------------')
    print('Denne studenten eksisterer allerede.')
    student_fil.close()

else:
    student_fil.close()
    student_fil = open('student.txt','a')

    fornavn = input('Skriv inn fornavn: ')
    etternavn = input('Skriv inn etternavn: ')
    studie = input('Skriv inn studiue: ')

    student_fil.write(studnr + '\n')
    student_fil.write(fornavn + '\n')
    student_fil.write(etternavn + '\n')
    student_fil.write(studie + '\n')

student_fil.close()

                    

            



