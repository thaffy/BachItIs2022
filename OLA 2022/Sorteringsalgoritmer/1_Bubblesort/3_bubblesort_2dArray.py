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