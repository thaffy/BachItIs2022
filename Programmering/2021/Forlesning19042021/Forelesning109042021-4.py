# Instansiere objektet med innlesing av data fra fil
# Serialisere og lagre objektet

import pickle

class Ansatt:
    def __init__(self,fornavn,etternavn,epost):
        self.__fornavn=fornavn
        self.__etternavn=etternavn
        self.__epost=epost

    def __str__(self):
        return 'Objektets attributter er: ' + self.__fornavn + '\n' + self.__etternavn + '\n' + self.__epost

ansatt_txt_fil=open('laerer.txt','r',encoding='utf-8')
ansatt_dat_fil=open('laerer.dat','wb')

fornavn=ansatt_txt_fil.readline()

while fornavn != '':
    
    fornavn=fornavn.rstrip('\n')
    etternavn=ansatt_txt_fil.readline().rstrip('\n')
    epost=ansatt_txt_fil.readline().rstrip('\n')

    # Oppretter objektet ny_ansatt
    ny_ansatt=Ansatt(fornavn,etternavn,epost)

    # Skriver ut attributtene til objektet
    print(ny_ansatt)

    # Seraliserer og lagrer
    pickle.dump(ny_ansatt,ansatt_dat_fil)

    fornavn=ansatt_txt_fil.readline()

ansatt_dat_fil.close()
ansatt_txt_fil.close()


    
    
