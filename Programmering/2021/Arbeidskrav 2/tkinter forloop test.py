from tkinter import *
from datetime import datetime
import mysql.connector
oblig2021database = mysql.connector.connect(host='localhost', port=3306, user='Eksamenssjef ', passwd='oblig2021', db='oblig2021')


window = Tk()
window.title('Karakterutskrift')

vitnemal_sql = ('SELECT Studentnr,Eksamensresultat.Emnekode,Emnenavn,MIN(Karakter),Studiepoeng \
                FROM Eksamensresultat,Emne \
                WHERE Eksamensresultat.Emnekode = Emne.Emnekode \
                    AND Studentnr = %s \
                GROUP BY Studentnr,Eksamensresultat.Emnekode,Emnenavn,Studiepoeng \
                ORDER BY SUBSTR(Eksamensresultat.Emnekode, -4) ASC')


def sokStudnr():
    for widget in window.winfo_children():
           widget.destroy()

    vitnemal_liste = []
    if vitnemal_liste:
        print('Har content')
    else:
        print('Har ikke content')
    vitnemal_markor = oblig2021database.cursor()
    studnr = input_studnr.get()

    vitnemal_data = (studnr,)

    vitnemal_markor.execute(vitnemal_sql,vitnemal_data)

    vitnemal_liste += vitnemal_markor

    navn_sql = ('SELECT Fornavn,Etternavn FROM Student WHERE Studentnr = %s')
    navn_data = (studnr,)
    vitnemal_markor.execute(navn_sql,navn_data)

    navn_liste = []
    navn_liste += vitnemal_markor
    fornavn = navn_liste[0][0]
    etternavn = navn_liste[0][1]

    input_navn = StringVar()
    input_navn.set(fornavn + ' ' + etternavn)
    lbl_navn = Label(window, textvariable = input_navn)
    lbl_navn.grid(row = 0, column = 1, padx = 10, pady = 5, sticky = W)

    listelengde = len(vitnemal_liste)

    poengsum = 0
    rad = 3
    emnekolonne = 0
    emnenavnkolonne = 1
    karakterkolonne = 2
    poengkolonne = 3

    listeteller = 0

    for row in range(listelengde):
        # Emnekomponenter
        emneset = StringVar()
        lbl_emne = Label(window,textvariable = emneset, width = 7)
        lbl_emne.grid(row = rad, column = emnekolonne, padx = 10, pady = 5, sticky = W)

        # Emnenavnkomponenter
        emnenavnset = StringVar()
        lbl_emnenavn = Label(window, textvariable = emnenavnset)
        lbl_emnenavn.grid(row = rad, column = emnenavnkolonne, padx = 10, pady = 5, sticky = W)

        # Karakterkomponenter
        karakterset = StringVar()
        lbl_karakter = Label(window, textvariable = karakterset, width = 2)
        lbl_karakter.grid(row = rad, column = karakterkolonne, padx = 10, pady = 5, sticky = W)

        # Poengkomponenter
        poengset = StringVar()
        lbl_poeng = Label(window, textvariable = poengset, width = 3)
        lbl_poeng.grid(row = rad, column = poengkolonne, padx = 10, pady = 5, sticky = W)
        
        

        emneset.set(vitnemal_liste[listeteller][1])
        emnenavnset.set(vitnemal_liste[listeteller][2])
        karakterset.set(vitnemal_liste[listeteller][3])

        if vitnemal_liste[listeteller][3] == 'F':
            poengset.set(0)
        else:
            poengset.set(vitnemal_liste[listeteller][4])
            poengsum += vitnemal_liste[listeteller][4]
        
        # Tellere - Poengsum summeres, raden øker og listetelleren øker.

        rad = rad + 1
        listeteller = listeteller + 1


    rad += 1

    lbl_totalsum = Label(window, text = 'Total Poengsum:')
    lbl_totalsum.grid(row = rad, column = 2, padx = 10, pady = 5, sticky = E)
    
    totalpoengsum = StringVar()
    totalpoengsum.set(poengsum)
    entry_totalsum = Entry(window, width = 4,state = 'readonly', textvariable = totalpoengsum)
    entry_totalsum.grid(row = rad, column = 3, padx = 10, pady = 5, sticky = W)
    
        


        



                   
        #print(vitnemal_liste[row][0],vitnemal_liste[row][1],vitnemal_liste[row][2],vitnemal_liste[row][3],vitnemal_liste[row][4])
        #poengsum = poengsum + (vitnemal_liste[row][4])


    

lbl_karakterUtskrift = Label(window,text = 'Karakterutskrift')
lbl_karakterUtskrift.grid(row = 0, column = 0, padx = 10, pady = 5, sticky = W)

lbl_emnekode = Label(window,text = 'Emnekode')
lbl_emnekode.grid(row = 2, column = 0, padx = 10, pady = 5, sticky = W)

lbl_emnenavn = Label(window,text = 'Emnenavn')
lbl_emnenavn.grid(row = 2, column = 1, padx = 10, pady = 5, sticky = W)

lbl_karakter = Label(window,text = 'Karakter')
lbl_karakter.grid(row = 2, column = 2, padx = 10, pady = 5, sticky = W)

lbl_studiepoeng = Label(window,text = 'Studiepoeng')
lbl_studiepoeng.grid(row = 2, column = 3, padx = 10, pady = 5, sticky = W)

input_studnr = StringVar()
entry_studnr = Entry(window, width = 6, textvariable = input_studnr)
entry_studnr.grid(row = 1, column = 1, padx = 10, pady = 5, sticky = W)


btn_sokStudnr = Button(window, text = 'Søk studentnr', command = sokStudnr)
btn_sokStudnr.grid(row = 1, column = 0, padx = 10, pady = 5, sticky = W)





    
