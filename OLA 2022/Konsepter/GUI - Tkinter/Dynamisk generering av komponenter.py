from tkinter import *


def main():
    hovedvindu = Tk()
    hovedvindu.title("Forloops")

    def lagreKarakter():
        for i in range(listelengde):
            if stringvarListe[i].get() != '':
                print('Studentnr:',studnrListe[i],'- Karakter:',stringvarListe[i].get())
            else:
                print('Kunne ikke lagre karakter for studentnr',studnrListe[i],'pga ugyldig verdi!')
                lbl_feil = Label(hovedvindu,text = '<- Feil!')
                lbl_feil.grid(row = i+1, column = 2, padx = 10, pady = 10, sticky = E)
                 
        print('---')
        print('Lagring ferdig!')
        print('---')

    studnrListe=['240229','240230','240231','240232','240233','240234']
    stringvarListe=[]
    listelengde = len(studnrListe)


    lbl_overskrift = Label(hovedvindu,text='Forlooping av komponenter')
    lbl_overskrift.grid(row = 0, columnspan = 2, padx = 10, pady = 10, sticky = E)

    for n in range(listelengde):
        studnr_output = StringVar()
        lbl_studnr = Label(hovedvindu, textvariable = studnr_output)
        lbl_studnr.grid(row = n+1, column = 0, padx = 10, pady = 10,sticky = E)
        studnr_output.set(studnrListe[n])

        karakter_input = StringVar()
        ent_karakter = Entry(hovedvindu, textvariable = karakter_input,width = 2)
        ent_karakter.grid(row = n+1, column = 1, padx = 10, pady = 10,sticky = W)
        stringvarListe += [karakter_input]

    btn_lagre = Button(hovedvindu,text = 'Lagre',command = lagreKarakter)
    btn_lagre.grid(row = n+2,columnspan = 2, padx = 10, pady = 10)

    btn_avslutt = Button(hovedvindu,text = 'Avslutt',command=hovedvindu.destroy)
    btn_avslutt.grid(row = n+3,column = 3, padx = 10, pady = 10)
    hovedvindu.mainloop()
    
    
main()
