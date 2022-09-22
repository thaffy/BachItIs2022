# Liste med scrollbar, to uavhengige komponenter som knyttes sammen
# i tillegg skal det vises ekstra informasjon når en velger i lista

from tkinter import *

def hent_epost(event):
    valgt = lst_ansatte.get(lst_ansatte.curselection())

    funnet = False
    radnr = 0

    # Finner riktig e-postadresse
    while (funnet==False) and (radnr<=len(ansatte)-1):
        if valgt == ansatte[radnr][0]:
            epost_til.set(ansatte[radnr][2])
            funnet = True
        else:
            radnr = radnr + 1
    

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

y_scroll = Scrollbar(window, orient = VERTICAL)
y_scroll.grid(row = 0, column = 2, rowspan = 5, padx = (0,100), pady = 5, sticky = NS)


innhold_i_lst_ansatte = StringVar()
lst_ansatte = Listbox(window, width = 10, height = 5, listvariable = innhold_i_lst_ansatte, yscrollcommand = y_scroll.set)
lst_ansatte.grid(row = 0, column = 1, rowspan = 5, padx = (100,0), pady = 5, sticky = E)
innhold_i_lst_ansatte.set(tuple(fornavn))
y_scroll["command"]=lst_ansatte.yview

epost_til = StringVar()
ent_epost = Entry(window,width = 30, state = 'readonly', textvariable = epost_til)
ent_epost.grid(row = 0, column = 3, sticky = E)
lst_ansatte.bind("<<ListboxSelect>>",hent_epost)


    

window.mainloop()
                      


