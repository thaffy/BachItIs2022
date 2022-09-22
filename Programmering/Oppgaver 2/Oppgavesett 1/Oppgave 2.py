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

