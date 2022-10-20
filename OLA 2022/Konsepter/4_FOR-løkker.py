### FOR-Løkke ###

# For-løkker er en måte å gjenta kode på.
# I en for-løkke definerer vi en løkketeller-variabel, og en øvre grense, eller limit, for hvor mange ganger løkka skal kjøre (loop!)

# I denne løkka er løkketeller-variabelen i, og limiten er 5.
# I praksis betyr det at løkka kjører 5 ganger, og at i øker med 1 for hver gang løkka kjører.
# i starter på null.

print("###")
print("Løkke 1: 5 ganger loop med i som løkkevariabel")
for i in range(5):
    print("For-løkka kjørte en loop! i =",i)
print("###")
print()



# Som vi kan se så starter løkka på 0 og går opp til 5, men IKKE til-og-med 5.
# For å få i til å være = 5 må vi setter range til 6, eller definere et startpunkt.
print("###")
print("Løkke 2: 6 ganger loop med i som løkkevariabel, i = 5 når løkka er ferdig")
for i in range(6):
    print("For-løkka kjørte en loop! i =",i)
print("###")
print()

print("###")
print("Løkke 3: 5 ganger loop med i som løkkevariabel, i = 1 ved løkke start og i = 5 ved løkke slutt.")
for i in range(1,6,1):
    print("For-løkka kjørte en loop! i =",i)
print("###")
print()



# Vi kan bruke løkke-telleren til kalkulering, referering til posisjon i liste, gjøre noe på et spesifikt tidspunkt osv.
# Vi definerer en listen med 3 personer:

liste = ["Markus","Terje","Sarah"]
print(liste)

# Via en FOR-løkke har vi lyst å skrive ut hvert navn, hver for seg, i rekkefølge.
# Vi kan bruke antall elementer i lista som limit via å definere en variabel:
listelengde = len(liste)

print("###")
for i in range(listelengde):
    print("For-løkka kjørte en loop! i =",i)
    print("Navnet på listeindex",i,"er: ",liste[i])
print("###")
print()

# I revers, altså at vi skriver lista ut i motsatt rekkefølge:
print("###")
for i in range(listelengde):
    print("For-løkka kjørte en loop! i =",i)
    print("Navnet på listeindex",listelengde-1,"minus i=",i,"=",listelengde-1-i,"er: ",liste[listelengde-1-i])
print("###")
print()