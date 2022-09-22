#Beregning av bruttolønn
#Først trenger vi input/inndata fra brukeren

timelonn=int(input('Hva er din timelønn? ')) # Unngå æ/ø/å i variabeler, men går disse greit i kommentarer og tekst som printes.
antall_timer=int(input('Hvor mange timer har du arbeidet? '))

#Bergner bruttolønn
bruttolonn=timelonn*antall_timer

#Skriver ut lønnsberegningen
print('Din bruttolønn er da',bruttolonn)

#Variabelnavn notasjon, enten antall_timer eller antallTimer ("LCC") - altså i sammensatte variabelnavn bruker man små bokstaver i første ord, og stor bokstav i andre ord
#når det er variabelnavn som er sammensatte av flere ord
#jfr lærebok side 66





