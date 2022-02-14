###############################################
# Sortering av en vanlig liste med tall.
liste = [1,5,4,7,12,78,67,54,3,2,55,43,32,13,14,1,90,87]
print(liste)

# For sortering bruker vi to forløkker med variablene i og j
# tenk på i som ytreløkke-teller og j som indreløkke-teller
# i praksis betyr dette at for hver gang i gjør én gjennomgang så gjør j x antall gjennomganger, 
# basert på telleren til i samt listelengden


listelengde = len(liste)

for i in range(listelengde-1): # <- Ytre løkke
    for j in range(0,listelengde-i-1): # <- Indre Løkke
        if liste[j] > liste[j+1]: # < - Sjekker om elementene skal byttes
            liste[j],liste[j + 1] = liste[j + 1], liste[j] # <- Gjør bytte
print(liste)
print()


###############################################
# Sortering av en to-dimensjonal liste med tall, basert på ett subelement's verdi
liste = [[1,2,5,4],[7,4,5,8],[12,5,3,7],[2,12,3,4],[3,12,6,4]]
print(liste)

listelengde = len(liste)
listeplass = 1 # <- Endre denne for å bytte subelement som det skal sorteres på!
               # Nå sorteres det på subelement 0 som i dette tilfettet 1,7,12,2,3 osv
               # Endrer vi listeplass til 1 så sorteres det på 2,4,5,12,12 osv

for i in range(listelengde):
    for j in range(0,listelengde-i-1):
        if liste[j][listeplass] > liste[j+1][listeplass]:
            liste[j],liste[j + 1] = liste[j + 1], liste[j]
print(liste)
print()

###############################################
# Sortering av en to-dimensjonal liste, hvor hvert subelement blir sortert internt
liste = [[1,2,5,4],[7,4,5,8],[12,5,3,7],[2,12,3,4],[3,12,6,4],[99,1,54,20]]
print(liste)

listelengde = len(liste)

for i in range(listelengde):
    for j in range(len(liste[i])):
        for k in range(len(liste[i])-j-1):
            if liste[i][k] > liste[i][k+1]:
                t = liste[i][k]
                liste[i][k] = liste[i][k+1]
                liste[i][k+1] = t
print(liste)
print()



