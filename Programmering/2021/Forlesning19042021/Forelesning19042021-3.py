# Objekter med flere dataattributter
# Instansiere objektet med verdier via variable og parameteroverføring
# setere og getere som metoder for å endre og skrive ut verdier på enkelt-attributt

# Serialisere og lagre objektet
# Importerer pickel-modulen for å serialisere/konvertere et objekt til en bit-strøm
# som kan lagres til fil for senere henting/bruk

import pickle

class Student:
    def __init__(self,studentnr,fornavn,etternavn,epost,studium):
        self.__studentnr=studentnr
        self.__fornavn=fornavn
        self.__etternavn=etternavn
        self.__epost=epost
        self.__studium=studium

    # Settere
    def set_studentnr(self,studentnr):
        self.__studentnr=studentnr

    def set_fornavn(self,fornavn):
        self.__fornavn=fornavn

    def set_etternavn(self,etternavn):
        self.__etternavn=etternavn

    def set_epost(self,epost):
        self.__epost=epost

    def set_studium(self,studium):
        self.__studium=studium


    # Gettere
    def get_studentnr(self):
        return self.__studentnr

    def get_fornavn(self):
        return self.__fornavn

    def get_etternavn(self):
        return self.__etternavn

    def get_epost(self):
        return self.__epost

    def get_studium(self):
        return self.__studium

    #__str__ metoden, holder orden på 'An object's state', dvs verdiene til attributtene
    def __str__(self):
        return 'Objektets attributter er: ' + self.__studentnr + '\n' + self.__fornavn + '\n' + self.__etternavn + '\n' + self.__epost + '\n' + self.__studium + '\n'

# Tar imot data i variable
studentnr=input('Oppgi studentnr: ')
fornavn=input('Oppgi fornavn: ')
etternavn=input('Oppgi etternavn: ')
epost=input('Oppgi epost: ')
studium=input('Oppgi studium: ')

# Instansierer nytt objekt
ny_student=Student(studentnr,fornavn,etternavn,epost,studium)

# Skriver ut attributtene til objektet
print(ny_student)


# Skriver ut epost og studium
print(ny_student.get_epost())
print(ny_student.get_studium())
print()

# Oppdatere epost og studium
epost=input('Oppgi ny-epost: ')
ny_student.set_epost(epost)
studium=input('Oppgi nytt studium: ')
ny_student.set_studium(studium)

# Skriver ut oppdaterte attributter til objektet
print(ny_student)

# Serialisering og skriving av objektet til fil
# Åpner en fil for binær skriving
# uten encoding - binary mode doesn't take encoding
studentfil=open('student.dat','wb')
# Pickler objektet (serialiserer det) og lagre på fil
pickle.dump(ny_student,studentfil)

# Lukker fila
studentfil.close()








