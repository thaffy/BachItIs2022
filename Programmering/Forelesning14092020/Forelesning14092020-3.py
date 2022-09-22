#Beregning av bruttolønn

#Inndata
timelonn=float(input('Hva er din timelønn? '))
antall_timer=float(input('Hvor mange timer har du arbeidet? '))

#Beregner bruttolønn
bruttolonn=timelonn*antall_timer

#Finner riktig skattesats

if bruttolonn<20000:
    skattesats=28
else:
    if bruttolonn<30000:
        skattesats=35
    else:
        skattesats=40

#Beregner skatt og netto lønn
skatt_i_kr=bruttolonn*skattesats/100
nettolonn=bruttolonn-skatt_i_kr

#Skriver ut lønnsberegninger
print('Din bruttolønn er',format(bruttolonn,'.2f'))
print('Din skatteprosent er',skattesats,'og skattetrekket i kroner er',format(skatt_i_kr,'.2f'))
print('Din nettolønn er',format(nettolonn,'.2f'),'kr')
