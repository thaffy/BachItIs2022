from tkinter import *
import mysql.connector

eksamendatabase = mysql.connector.connect(host='localhost',port=3306,user='Dekksjef',passwd='eksamen2021',db='Dekkhotell')

markor = eksamendatabase.cursor()
oppbevaringsql = ('SELECT * FROM Oppbevaring WHERE Utlevert IS NULL ORDER BY Innlevert')
markor.execute(oppbevaringsql)

oppbevaringliste = []
oppbevaringliste += markor

listelengde1 = len(oppbevaringliste)

regnrliste = []

for row range(listelengde):
    regnrliste += oppbevaringliste[row][1]








hovedvindu = Tk()
hovedvindu.title('Oppgave 2 - Oppbevaringer Dekkhotell')

y_scroll = Scrollbar(hovedvindu, orient=VERTICAL)
y_scroll.grid(row = 0, column = 2, rowspan = 5, padx = (0,100), pady = 5, sticky =  NS)

innhold_i_lst_regnr = StringVar()
lst_regnr = Listbox(hovedvindu, width = 10, height = 5, listvariable = innhold_i_lst_regnr,yscrollcommand = y_scroll.set)
lst_regnr.grid(row = 0, column = 1, rowspan = 5, padx = (100,0), pady = 5,sticky = E)
y_scroll["command"] = lst_regnr.yview

lbl_mobilnr = Label(hovedvindu, text = 'Mobilnr: ')
lbl_mobilnr.grid(row = 0, column = 2, padx = 10, pady = 5, sticky = E)

lbl_etternavn = Label(hovedvindu, text = 'Etternavn: ')
lbl_etternavn.grid(row = 1, column = 2, padx = 10, pady = 5, sticky = E)

lbl_epost = Label(hovedvindu, text = 'Epost: ')
lbl_epost.grid(row = 2, column = 2, padx = 10, pady = 5, sticky = E)

lbl_hylle = Label(hovedvindu, text = 'Hylle: ')
lbl_hylle.grid(row = 3, column = 2, padx = 10, pady = 5, sticky = E)


output_mobilnr = StringVar()
ent_mobilnr = Entry(hovedvindu, width = 8,state = 'readonly', textvariable = output_mobilnr)
ent_mobilnr.grid(row = 0, column = 3, padx = 10, pady = 5, sticky = W)

output_etternavn = StringVar()
ent_etternavn = Entry(hovedvindu, width = 20, state = 'readonly', textvariable = output_etternavn)
ent_etternavn.grid(row = 1, column = 3, padx = 10, pady = 5, sticky = W)

output_epost = StringVar()
ent_epost = Entry(hovedvindu, width = 20, state = 'readonly', textvariable = output_epost)
ent_epost.grid(row = 2, column = 3, padx = 10, pady = 5, sticky = W)

output_hylle = StringVar()
ent_hylle = Entry(hovedvindu, width = 5, state = 'readonly', textvariable = output_hylle)
ent_hylle.grid(row = 3, column = 3, padx = 10, pady = 5, sticky = W)


btn_avslutt = Button(hovedvindu, text = 'Avslutt',command = hovedvindu.destroy)
btn_avslutt.grid(row = 4, column = 3, padx = 10, pady = 5, sticky = E)

hovedvindu.mainloop()


