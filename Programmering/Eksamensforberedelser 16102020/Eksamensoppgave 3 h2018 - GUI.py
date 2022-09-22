
from tkinter import *
window = Tk()

def beregn_utbetalt():

    manedslonn=int(input_manedslonn.get())
    
    if manedslonn <= 20000:
        skatt = 0.00
    else:
        if manedslonn <= 35000:
            skatt = 0.28
        else:
            if manedslonn <= 50000:
                skatt = 0.35
            else:
                if manedslonn <= 70000:
                    skatt = 0.42
                else:
                    skatt = 0.48
                    
    beregn_utbetalt=manedslonn*(1-skatt)
    utbetalt.set(beregn_utbetalt)


# Vindunavn
window.title('Lønnskalkulator')


# Månedslønn
lbl_manedslonn = Label(window, text='Månedslønn:')
lbl_manedslonn.grid(row = 0, column = 0, padx = 100, pady = 15)

input_manedslonn=StringVar()
ent_manedslonn = Entry(window, width = 9, textvariable=input_manedslonn)
ent_manedslonn.grid(row = 0, column = 1, padx = 100, pady = 15)

btn_beregn = Button(window, text='Beregn utbetalt', command=beregn_utbetalt)
btn_beregn.grid(row = 0, column = 2, columnspan = 2, pady=15)


# Utbetalt
lbl_utbetalt = Label(window, text='Utbetalt:')
lbl_utbetalt.grid(row = 1, column = 0, padx = 100, pady = 15)

utbetalt=StringVar()
ent_utbetalt = Entry(window, width= 9, state='readonly', textvariable=utbetalt)
ent_utbetalt.grid(row = 1, column = 1, padx = 100, pady = 15)

# Avslutt
btn_avslutt = Button(window, text='Avslutt', command=window.destroy)
btn_avslutt.grid(row = 4, column = 3, columnspan = 2, pady = 15)



window.mainloop()
