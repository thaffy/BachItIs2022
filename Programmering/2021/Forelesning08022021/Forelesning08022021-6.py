# Listebokskomponenten
# Lese data fra fil til tabell og legger deler av tabellen i en ny liste som vises
# i en listeboks, det er flere elementer i lista enn det som vises
# Mulig å scrolle i lista, men ingen indikasjon på det.

from tkinter import *

# Oppretter global liste
ansatte = []
ansattfil = open('Laerer.txt','r',encoding='utf-8')

fornavn = ansattfil.readline()

while fornavn != '':
    fornavn = fornavn.rstrip('\n')

    etternavn = ansattfil.readline().rstrip('\n')
    epost = ansattfil.readline().rstrip('\n')

    ansatte += [[fornavn,etternavn,epost]]

    fornavn = ansattfil.readline()
    
ansattfil.close()

# Lager fornavnlista fra tabellen
fornavn = []
for listelengde in range(0,len(ansatte),1):
    fornavn += [ansatte[listelengde][0]]

window = Tk()
window.title('Ansatte')

innhold_i_lst_ansatte = StringVar()
lst_ansatte = Listbox(window, width = 10, height = 5, listvariable = innhold_i_lst_ansatte)
lst_ansatte.grid(padx = 100, pady = 5)
innhold_i_lst_ansatte.set(tuple(fornavn))

window.mainloop()
                      


