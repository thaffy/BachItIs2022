# Program for å lese 5 tall inn i en liste og finne det minste tallet

# tallliste defineres som en tom liste
tallliste=[]

# Utskrift av listeinnhold før fylling
print('Lista til nå:',tallliste)
print()

# FOR-løkke for å lese inn 5 tall i lista tallliste. Alle print-setningene i FOR-løkka kan utelattes, kun til kontroll.
for index in range(0,5,1):
    print('Tall nr:',index+1)
    listeverdi=int(input('Oppgi tall: '))
    # Innlest verdi legges inn i lista
    tallliste +=[listeverdi]
    # Utskrift av listeinnhold underveis/med fylling
    print('Lista til nå:',tallliste)
    print()

# Utskrift av listeinnhold og listestørrelse etter fylling
print('Hele lista er:',tallliste)
liste_lengde=len(tallliste)
print('Antall elementer i lista er:',liste_lengde)

# Prøv selv/oppgave til neste gang
# Utvid programmet til å finne minste tall og tallnr i lista - Sjekk program-2

minste_tall=tallliste[0]
tallnr=1

for index in range(1,5,1):
    if tallliste[index]<minste_tall:
        # Da er det et nytt tall som er minste tall
        minste_tall=tallliste[index]
        # Tallnr i rekka er indpex i lista pluss 1
        tallnr=index+1

print('Det minste tallet er',minste_tall,'og det er tall nr',tallnr,'i lista.')
