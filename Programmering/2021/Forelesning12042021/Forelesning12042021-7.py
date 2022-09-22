# Bankkonto

# Flere objekter/instanser av samme klasse, her: kontoene til flere personer

# Bankkontro-klassen simulerer en bankkonto
class BankKonto:
    # __init__ metoden tar imot et argument for saldo
    # Det blir tilordna saldo attributtet
    def __init__(self,saldo):
        self.__saldo=saldo

    # innskudd metoden setter et innskudd inn på konto
    def innskudd(self,belop):
        self.__saldo=self.__saldo + belop

    # uttak metoden foretar et uttak på konto hvis nok penger
    def uttak(self,belop):
        if self.__saldo>=belop:
            self.__saldo=self.__saldo-belop
        else:
            print('Feil: ikke nok på konto')

    # hent_saldo metoden returnerer saldoen på kontoen
    def hent_saldo(self):
        return self.__saldo

def main():
    # Oppgi startsaldo på konto for Kari
    saldo = float(input('Hva er saldo på konto til Kari? '))

    # Opprett et bankkonto objekt for Kari
    karis_konto = BankKonto(saldo)

    # Oppgi startsaldo for konto til Knut
    saldo = float(input('Hva er saldoen på konto to Knut Ivar? '))
    knuts_konto = BankKonto(saldo)


    belop = float(input('Hvor mye skal Kari sette inn på konto? '))
    karis_konto.innskudd(belop)
    print('Saldoen på kontoen til Kari er:',karis_konto.hent_saldo())

main()
        
