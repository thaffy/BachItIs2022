from tkinter import *
import mysql.connector

eksamendatabase = mysql.connector.connect(host='localhost',port=3306,user='Dekksjef',passwd='eksamen2021',db='Dekkhotell')

hovedvindu = Tk()
hovedvindu.title('Oppgave 3 - Registrer Kunde')

def lagreKunde():

    mobilnr = input_mobilnr.get()
    fornavn = input_fornavn.get()
    etternavn = input_etternavn.get()
    epost = input_epost.get()

    regnr = input_regnr.get()
    innlevert = input_innlevert.get()
    pris = input_pris.get()
    hylle = input_hylle.get()

    kunde_markor = eksamendatabase.cursor()
    kunde_markor.execute('SELECT * FROM Kunde')

    kundesjekk_liste = []
    kundesjekk_liste += kunde_markor

    listelengde = len(kundesjekk_liste)

    duplikat = False

    for row in range(listelengde):
        if mobilnr == kundesjekk_liste[row][0]:
            duplikat = True


    if duplikat == False:
        settinn_kunde = ('INSERT INTO Kunde VALUES(%s,%s,%s,%s)')
        kunde_data = (mobilnr,fornavn,etternavn,epost)
        kunde_markor.execute(settinn_kunde,kunde_data)

        settinn_dekksett = ('INSERT INTO Dekksett VALUES(%s,%s)')
        dekksett_data = (mobilnr, regnr)
        kunde_markor.execute(settinn_dekksett,dekksett_data)

        settinn_oppbevaring = ('INSERT INTO Oppbevaring VALUES')

    

    
    
    


# GUI

lbl_mobilnr = Label(hovedvindu, text = 'Mobilnr: ')
lbl_mobilnr.grid(row = 0, column = 0, padx = 10, pady = 5, sticky = E)

lbl_fornavn = Label(hovedvindu, text = 'Fornavn: ')
lbl_fornavn.grid(row = 1, column = 0, padx = 10, pady = 5, sticky = E)

lbl_etternavn = Label(hovedvindu, text = 'Etternavn: ')
lbl_etternavn.grid(row = 2, column = 0, padx = 10, pady = 5, sticky = E)

lbl_epost = Label(hovedvindu, text = 'Epost: ')
lbl_epost.grid(row = 3, column = 0, padx = 10, pady = 5, sticky = E)

lbl_regnr = Label(hovedvindu, text = 'Regnr: ')
lbl_regnr.grid(row = 4, column = 0, padx = 10, pady = 5, sticky = E)

lbl_innlevert = Label(hovedvindu, text = 'Innlevert: ')
lbl_innlevert.grid(row = 5, column = 0, padx = 10, pady = 5, sticky = E)

lbl_pris = Label(hovedvindu, text = 'Pris ')
lbl_pris.grid(row = 6, column = 0, padx = 10, pady = 5, sticky = E)

lbl_hylle = Label(hovedvindu, text = 'Hylle: ')
lbl_hylle.grid(row = 7, column = 0, padx = 10, pady = 5, sticky = E)



input_mobilnr = StringVar()
ent_mobilnr = Entry(hovedvindu,width = 8)
ent_mobilnr.grid(row = 0, column = 1, padx = 10, pady = 5, sticky = W)

input_fornavn = StringVar()
ent_fornavn = Entry(hovedvindu,width = 8)
ent_fornavn.grid(row = 1, column = 1, padx = 10, pady = 5, sticky = W)

input_etternavn = StringVar()
ent_etternavn = Entry(hovedvindu,width = 8)
ent_etternavn.grid(row = 2, column = 1, padx = 10, pady = 5, sticky = W)

input_epost = StringVar()
ent_epost = Entry(hovedvindu,width = 8)
ent_epost.grid(row = 3, column = 1, padx = 10, pady = 5, sticky = W)

input_regnr = StringVar()
ent_regnr = Entry(hovedvindu,width = 8)
ent_regnr.grid(row = 4, column = 1, padx = 10, pady = 5, sticky = W)

input_innlevert = StringVar()
ent_innlevert = Entry(hovedvindu,width = 8)
ent_innlevert.grid(row = 5, column = 1, padx = 10, pady = 5, sticky = W)

input_pris = StringVar()
ent_pris = Entry(hovedvindu,width = 8)
ent_pris.grid(row = 6, column = 1, padx = 10, pady = 5, sticky = W)

input_hylle = StringVar()
ent_hylle = Entry(hovedvindu,width = 8)
ent_hylle.grid(row = 7, column = 1, padx = 10, pady = 5, sticky = W)

btn_lagre = Button(hovedvindu, text = 'Lagre',command=lagreKunde)
btn_lagre.grid(row = 8, column = 1, padx = 10, pady = 5, sticky = W)

btn_avslutt = Button(hovedvindu, text = 'Avslutt')
btn_avslutt.grid(row = 9, column = 2, padx = 10, pady = 5, sticky = E)









