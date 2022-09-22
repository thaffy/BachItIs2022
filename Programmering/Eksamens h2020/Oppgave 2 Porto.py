
from tkinter import *
window = Tk()

def beregn_porto():

    # Gjør om input_vekt som er en string til en int
    vekt = int(input_vekt.get())

    if vekt <= 20:
        porto = 17
    elif vekt <= 50:
        porto = 24
    elif vekt <= 100:
        porto = 27
    elif vekt <= 350:
        porto = 45
    elif vekt <= 1000:
        porto = 88
    else:
        porto = 125

    output_porto.set(porto)



# Vindunavn

window.title('Portokalkulator')

# Label, entry og button for øverste rad
lbl_vekt = Label(window, text='Forsendelsens vekt (i gram):')
lbl_vekt.grid(row = 0, column = 0, padx = 10, pady = 15)

input_vekt = StringVar()
ent_vekt = Entry(window, width = 9, textvariable=input_vekt)
ent_vekt.grid(row = 0, column = 1, padx = 50, pady = 15)

btn_beregn = Button(window, text='Beregn porto', command=beregn_porto)
btn_beregn.grid(row = 0, column = 2, columnspan = 1, pady = 15)

# Label og entry for neste rad
lbl_porto = Label(window, text='Porto:')
lbl_porto.grid(row = 1, column = 0, padx = 10, pady = 15)

output_porto=StringVar()
ent_porto = Entry(window, width = 5, state='readonly', textvariable=output_porto)
ent_porto.grid(row = 1, column = 1, padx = 10, pady = 15)

# Button for avslutt

btn_avslutt = Button(window, text='Avslutt', command = window.destroy)
btn_avslutt.grid(row = 2, column = 2, columnspan = 1, pady = 15)

window.mainloop()


                






