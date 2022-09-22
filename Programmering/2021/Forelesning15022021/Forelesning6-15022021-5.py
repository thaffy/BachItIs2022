# Introduksjon til GUI-programmering
# Grunnstruktur
# Med komponentene ledetekst, inndatafelt, utdatafelt og knapp
# Laget en avslutt-knapp for å slippe å bruke "lukk vindu"

# Nytt i program ...6-4
# Endret padx = 10 og pady = 5 på gridelementene, knappene
# Fjernet columnspan = 2 på begge knappene og plassert de i column 1

# Nytt i program ...6-5
# Høyrejustere ledetekstene i kolonne 1 og venstrejustere tekstfeltene i kolonne 2
# sticky = E (høyre) for ledetekstene i kolonne 1
# og sticky = W (venstre) for tekstfeltene i kolonne 2
# Plassere beregn lånetilsang-knappen venstrejustert i kolonne 2
# og avsluttknappen høyrejustert i kolonne 2

from tkinter import *
window = Tk()

def beregn_lan():
    if int(egenkapital.get())/int(kjopesum.get())>=0.35:
        lanetilsagn.set('Lån innvilges')
    else:
        lanetilsagn.set('Lån innvilges ikke')




# Vi gir vinduet et navn
window.title('Lånekalkulator billån')

# Vi lager ledetekster for kjøpesum, egenkapital og lånetilsagn
lbl_kjopesum=Label(window, text='Kjøpesum:')
lbl_kjopesum.grid(row=0, column=0, padx=10, pady=5, sticky = E)

lbl_egenkapital=Label(window, text='Egenkapital:')
lbl_egenkapital.grid(row=1, column=0, padx=10, pady=5, sticky = E)

lbl_lanetilsagn=Label(window, text='Lånetilsagn:')
lbl_lanetilsagn.grid(row=3, column=0, padx=10, pady=5, sticky = E)

# Vi lager inndatafelt for kjøpesum og egenkapital
kjopesum=StringVar()
ent_kjopesum=Entry(window, width=9, textvariable=kjopesum)
ent_kjopesum.grid(row=0, column=1, padx=10, pady=5, sticky = W)

egenkapital=StringVar()
ent_egenkapital=Entry(window, width=9, textvariable=egenkapital)
ent_egenkapital.grid(row=1, column=1, padx=10, pady=5, sticky = W)

# Vi lager knapp for å beregne lånetilsagnet
btn_beregn=Button(window, text='Beregn lånetilsagn',command=beregn_lan)
btn_beregn.grid(row=2,column=1,padx=10, pady=5, sticky = W)

# Og vi lager utdatafelt/visningsfelt for konklusjonen på lånetilsagnet.
lanetilsagn=StringVar()
ent_lanetilsagn=Entry(window, width=20, state='readonly', textvariable=lanetilsagn)
ent_lanetilsagn.grid(row=3, column=1,padx=10,pady=5, sticky = W)

# Knapp for å avslutte
btn_avslutt=Button(window, text='Avslutt', command=window.destroy)
btn_avslutt.grid(row=5, column=1,padx=10,pady=5, sticky = E)

# Prøv på egenhånd
# 1) Samle definisjon av ledetekst, komponent og variabel for de som hører sammen.
# 2) Legge kode for vinduet i main og kall av main

# Ledetekst - venstremarg
# Inndatafelt - høyremarg
# Avslutt-knapp = nederst til høyre

window.mainloop()
