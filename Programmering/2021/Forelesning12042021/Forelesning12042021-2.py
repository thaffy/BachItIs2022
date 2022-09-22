# Program for brukerbestemt antall myntkast og opptelling av antall Krone og Myn
# objekt-orientert tilnærming, hvor metoder håndterer egenskaper ved mynten
# og programlogikken/"spillet" ligger i main()

import random

# Mynt-klassen simulerer en mynt og hva vi kan gjøre med den
class Mynt:
    # __init__ metoden initierer objektet/forekomsten/instansen
    # og tilordner sideopp-attributtet startverdien 'Krone' (self.sideopp),
    # dvs setter en startverdi som ikke skal telles med
    def __init__(self):
        self.sideopp='Krone'


    # kastmetoden simulerer ett kast med mynten
    # og gir sideopp-attributtet ny verdi
    def kast(self):
        if random.randint(0,1)==0:
            self.sideopp='Krone'
        else:
            self.sideopp='Mynt'


    # hent_sideopp metoden returnerer tul enhver tid
    # verdien("siste verdi") på mynten, dvs sideopp-attributtet
    def hent_sideopp(self):
        return self.sideopp






def main():
    antall_kron = 0
    antall_mynt = 0

    # Oppretter et mynt_objekt, en forekomst/instanse
    min_mynt = Mynt()

    print('Før første kast er denne siden opp:',min_mynt.hent_sideopp())

    antall_kast = int(input('Hvor mange ganger skal mynten kastes? '))

    for antall_ganger in range(1,antall_kast+1,1):
        # Mynten kastes
        min_mynt.kast()
        #print('Resultat av kast nr',antall_ganger,'ble',min_mynt.hent_sideopp())

        if min_mynt.hent_sideopp()=='Krone':
            antall_kron += 1

        else:
            antall_mynt += 1

    print('Resultatet av forsøksrekka ble',antall_kron,'Krone og',antall_mynt,'Mynt')

main()
