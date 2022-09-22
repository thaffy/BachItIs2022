class Kunde:
    def __init__(self,mobilnr,fornavn,etternavn,epost):
        self.__mobilnr=mobilnr
        self.__fornavn=fornavn
        self.__etternavn=etternavn
        self.__epost=epost

    # Sette
    def set_mobilnr(self,mobilnr):
        self.__mobilnr=mobilnr

    def set_fornavn(self,fornavn):
        self.__fornavn=fornavn

    def set_etternavn(self,etternavn):
        self.__etternavn=etternavn

    def set_epost(self,epost):
        self.__epost=epost

    # Gettere

    def get_mobilnr(self):
        return self.__mobilnr
    
    def get_fornavn(self):
        return self.__fornavn

    def get_etternavn(self):
        return self.__etternavn

    def get_epost(self):
        return self.__epost

    # __str__ metoden for return av alle attributtene
    def __str__(self):
        return 'Objektets attributter er: ' + '\n' + self.__mobilnr + '\n' + self.__fornavn + '\n' + self.__etternavn + '\n' + self.__epost

mobilnr = input('Oppgi mobilnr: ')
fornavn = input('Oppgi fornavn: ')
etternavn = input('Oppgi etternavn: ')
epost = input('Oppgi epost: ')

ny_kunde = Kunde(mobilnr,fornavn,etternavn,epost)
print(ny_kunde)
    
    
    



        