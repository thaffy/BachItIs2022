from tkinter import *
# Definerer vinduet
window = Tk()

def lanekalkulator():
    # All kode relatert til selve utregningen er plassert i denne funksjonen.
    
    # If-test på om bruker har endret på sliderne/skrevet inn noen verdier høyere enn default (0).
    # Hvis bruker ikke har gjort noe med har trykket på beregn så spør programmet om å skrive inn noen verdier først.
    if (kjopesum.get() == '0' and egenkapital.get() == '0') or (kjopesum.get() == '0') or (egenkapital.get() == '0'):
        innvilges.set('Skriv inn verdier!')
        lbl_innvilges['fg']='orange'
    else:

        # Etter at noen verdier har blitt gitt på både bilpris og egenkapital kan programmet begynne med utregninger.
        bilpris=int(kjopesum.get())
        bruker_egenkapital=int(egenkapital.get())

        

        egenkapital_prosent=(bruker_egenkapital/bilpris)*100

        if egenkapital_prosent<35:
            innvilges.set('Lån kan ikke innvilges!')
            lbl_innvilges['fg']='red'
            rente.set(0)
            terminer.set(0)
            terminbelop.set(0)
        else:
            innvilges.set('Lån innvilges!')
            lbl_innvilges['fg']='green'
            if egenkapital_prosent>=35 and egenkapital_prosent<50:
                arlig_rente=4.5
            else:
                if egenkapital_prosent>=50 and egenkapital_prosent<60:
                    arlig_rente=3
                else:
                    arlig_rente=2.5

            # Skriver ut renten til bruker, med %-tegn
            rente.set(format(arlig_rente/100,'.1%'))

            # Henter hvor mange år bruker har valgt via input og/eller slider
            nedbetaling=int(antall_aar.get())

            lanesum=bilpris-bruker_egenkapital
            antall_terminer=nedbetaling*12

            # Oppdaterer utdatafeltet med antall terminer i måender
            terminer.set(antall_terminer)

            termin_rente=(arlig_rente/12)/100
            termin_belop=lanesum*((1+termin_rente)**antall_terminer)*termin_rente/(((1+termin_rente)**antall_terminer)-1)

            # Oppdaterer utdatafeltet med terminbeløpet, formatert til .00
            terminbelop.set("{:,.2f}".format(termin_belop) + ' kr')


    

# Gir navn til vinduet
window.title('Billånskalkulator')

# Ledetekst for kjøpesum, egenkapital og nedbetalingstid i år
lbl_kjopesum=Label(window,text='Kjøpesum:')
lbl_kjopesum.grid(row=0,column=0,padx=5,pady=5,sticky=E)

lbl_egenkapital=Label(window,text='Egenkapital:')
lbl_egenkapital.grid(row=2,column=0,padx=5,pady=5,sticky=E)

lbl_antall_aar=Label(window,text='Nedbetalingstid:')
lbl_antall_aar.grid(row=4,column=0,padx=5,pady=(5,0),sticky=E)

# Entryfelt for kjøpesum, egenkapital og nedbetalingstid
kjopesum=StringVar()
ent_kjopesum=Entry(window,width=9,textvariable=kjopesum)
ent_kjopesum.grid(row=0,column=1,padx=5,pady=(5,0),sticky=W)

egenkapital=StringVar()
ent_egenkapital=Entry(window,width=9,textvariable=egenkapital)
ent_egenkapital.grid(row=2,column=1,padx=5,pady=(5,0),sticky=W)

antall_aar=StringVar()
ent_antall_aar=Entry(window,width=2,textvariable=antall_aar)
ent_antall_aar.grid(row=4,column=1,padx=5,pady=(5,0),sticky=W)

# Scale-bar for å velge antall år hvis man vil
scale_kjopesum=Scale(orient=HORIZONTAL,length=100,from_=0,to=1000000,variable=kjopesum,command=kjopesum,showvalue=0,resolution=10000)
scale_kjopesum.grid(row=1,columnspan=2,padx=5,pady=(0,5),sticky='WE')

scale_egenkapital=Scale(orient=HORIZONTAL,length=100,from_=0,to=1000000,variable=egenkapital,command=egenkapital,showvalue=0,resolution=10000)
scale_egenkapital.grid(row=3,columnspan=2,padx=5,pady=(0,5),sticky='WE')

scale_antall_aar=Scale(orient=HORIZONTAL,length=100,from_=1,to=15,variable=antall_aar,command=antall_aar,showvalue=0)
scale_antall_aar.grid(row=5,columnspan=2,padx=5,pady=0,sticky='WE')

# Entry boks i read-only for å fortelle bruker om lånet innvilges
innvilges=StringVar()
lbl_innvilges=Label(window,width=16,textvariable=innvilges)
lbl_innvilges.grid(row=6,columnspan=2,padx=5,pady=5)

# Ledetekst for lån innvilges, årlig rente, antall terminer og terminbeløp
lbl_rente=Label(window,text='Årlig rente:')
lbl_rente.grid(row=7,column=0,padx=5,pady=5,sticky=E)

lbl_terminer=Label(window,text='Antall terminer:')
lbl_terminer.grid(row=8,column=0,padx=5,pady=5,sticky=E)

lbl_termin_belop=Label(window,text='Terminbeløp:')
lbl_termin_belop.grid(row=9,column=0,padx=5,pady=5,sticky=E)

# Entryfelt i read-only for utskrift av beregninger
rente=StringVar()
ent_rente=Entry(window,width=4,textvariable=rente,state='readonly')
ent_rente.grid(row=7,column=1,padx=5,pady=5,sticky=W)

terminer=StringVar()
ent_terminer=Entry(window,width=3,textvariable=terminer,state='readonly')
ent_terminer.grid(row=8,column=1,padx=5,pady=5,sticky=W)

terminbelop=StringVar()
ent_termin_belop=Entry(window,width=10,textvariable=terminbelop,state='readonly')
ent_termin_belop.grid(row=9,column=1,padx=5,pady=5,sticky=W)

# Button for å beregne og for å avslutte
btn_beregn=Button(window,text='Beregn lån',command=lanekalkulator)
btn_beregn.grid(row=10,column=1,padx=5,pady=5, sticky=W)

btn_avslutt=Button(window,text='Avslutt',command=window.destroy)
btn_avslutt.grid(row=11,column=1,padx=5,pady=(25,5),sticky=E)


# Loop for vinduet
window.mainloop()
