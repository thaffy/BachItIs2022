# Oppgave 3
# Norsk matematikkråd har følgende retningslinjer for karaktersetting i kvantitative fag på Bachelornivå («poeng av 100»).

# Karakter	Poeng
# A	         92
# B	         77
# C	         58
# D	         46
# E	         40
# Lag et program som på bakgrunn av poengsum som inndata viser kandidatens karakter i emnet.

antall_poeng=int(input('Hvor mange poeng skal gjøres om til karakter? '))

if antall_poeng<40:
    karakter=('F')
else:
    if antall_poeng<46:
        karakter=('E')
    else:
        if antall_poeng<58:
            karakter=('D')
        else:
            if antall_poeng<77:
                karakter=('C')
            else:
                if antall_poeng<92:
                    karakter=('B')
                else:
                    karakter=('A')

print('Med',antall_poeng,'poeng blir karakteren satt til karakteren',karakter)



    
