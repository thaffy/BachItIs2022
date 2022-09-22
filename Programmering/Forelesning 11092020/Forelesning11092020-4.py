#Program 2-17, alternativ 2
#Samme stategi som i alternativ 1

antall_sekunder=int(input('Oppgi antall sekunder som skal konverteres: '))

#Beregninger
antall_timer=antall_sekunder//3600
resterende_sekunder_etter_timer=antall_sekunder%3600

antall_minutter=resterende_sekunder_etter_timer//60
resterende_sekunder_etter_minutter=resterende_sekunder_etter_timer%60

#Utskrift av resultat
print(antall_sekunder,'sekunder gjort om til timer, minutter og sekunder blir:')
print('Timer:',antall_timer)
print('Minutter',antall_minutter)
print('Sekunder',resterende_sekunder_etter_minutter)
