# Oppgave 2
# Et bilutleiefirma tilbyr følgende alternativer for dagsleie av leiebil:
# 1. fastpris 750 kr
# 2. fastpris 300 kr og 2 kr pr kjørt km
# 3. fastpris 150 kr og 4 kr pr kjørt km
# Kunden må velge et av alternativene ved inngåelse av leiekontrakten.
# Lag et program som sammenligner de tre alternativene ut fra antall km som inndata, og avgjør hvilket alternativ som er best for kunden.

# Henter antall kilometer som skal kjøres fra bruker.
antall_km=int(input('Hvor mange kilometer skal du kjøre? '))

# Beregner pris for alternativene, med betaling for antall kilometer for alternativ 2 og 3.
alternativ_1=750
alternativ_2=300+2*antall_km
alternativ_3=150+4*antall_km

# Sammenligner prisene og skriver ut den minste.
if alternativ_1<alternativ_2:
    print('Alternativ 1 blir det beste for deg. Da blir prisen',alternativ_1,'kr.')
else:
    if alternativ_2<alternativ_3:
        print('Alternativ 2 er det beste for deg. Da blir prisen',alternativ_2,'kr.')
    else:
        print('Alternativ 3 er det beste for deg. Da blir prisen',alternativ_3,'kr.')
print()




for i in range(0,550,50):
    pris1 = 750
    pris2 = 350 + (2*i)
    pris3 = 150 + (4*i)

    print('Antall km kjørt:',i,'km.')
    print('Alternativ 1 koster:',pris1)
    print('Alternativ 2 koster:',pris2)
    print('Alternativ 3 koster:',pris3)
    print('---')
    if pris1<pris2:
        print('Alternativ 1 blir det beste for deg. Da blir prisen',pris1,'kr.')
    else:
        if pris2<pris3:
            print('Alternativ 2 er det beste for deg. Da blir prisen',pris2,'kr.')
        else:
            print('Alternativ 3 er det beste for deg. Da blir prisen',pris3,'kr.')
    print('---')
    print()
    

