#Eksempel på bruk av command-attributtet

#Button komponenten har et command-argument som binder kallet av funksjonen når
#en handling utføres
def bytt_farge():
    if btn_byttFarge['fg']=='blue':
        btn_byttFarge['fg']='red'
    else:
        btn_byttFarge['fg']='blue'





from tkinter import *

vindu=Tk()
vindu.title('Knapp for fargevalg')

#Første komponenten i konstruktør er 'vindu'
btn_byttFarge=Button(vindu,text='Bytt farge',fg='blue',command=bytt_farge)
btn_byttFarge.grid(padx=75,pady=15)


vindu.mainloop()
