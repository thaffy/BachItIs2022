from tkinter import *

def main():
    hovedvindu = Tk()
    hovedvindu.title('Test-program')
     stringvars = []
    studnrListe = ['240240','240241','240242']

    def lagreKarakter():
        for n in range(len(stringvars)):
            if stringvars[n].get() != '':
                print(studnrListe[n],':',stringvars[n].get())

    lbl_overskrift = Label(hovedvindu,text='Registrer karakter for eksamener')
    lbl_overskrift.grid(row=0,column=1,padx=10,pady=10)

    listelengde = len(studnrListe)
    
    for n in range(listelengde):
        studnrEntry = StringVar()
        ent_studnr = Label(hovedvindu,width = 6, textvariable = studnrEntry)
        ent_studnr.grid(row = n+1, column = 0, padx = 10, pady = 10, sticky = E)
        studnrEntry.set(studnrListe[n])

        inputEntry = StringVar()
        ent_karakter = Entry(hovedvindu,width = 1, textvariable = inputEntry)
        ent_karakter.grid(row = n+1, column = 1, padx = 10, pady = 10, sticky = W)
        stringvars += [inputEntry]
        
    btn_lagre = Button(hovedvindu,text='Lagre',command=lagreKarakter)
    btn_lagre.grid(row = n+2, column = 0, padx = 10, pady = 10)

    btn_tilbake = Button(hovedvindu,text='Gå Tilbake', command=hovedvindu.destroy)
    btn_tilbake.grid(row=n+2, column = 1, padx = 10, pady = 10)

    hovedvindu.mainloop()

main()
