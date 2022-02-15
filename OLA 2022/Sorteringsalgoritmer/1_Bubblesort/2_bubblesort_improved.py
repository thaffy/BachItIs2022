
liste = [10,1,6,3,4]
listelengde = len(liste)
print(liste)

for i in range(listelengde): # <- Ytre løkke
    bytte = False
    for j in range(0,listelengde-i-1): # <- Indre Løkke
        if liste[j] > liste[j+1]: # < - Sjekker om elementene skal byttes
            liste[j],liste[j + 1] = liste[j + 1], liste[j] # <- Gjør bytte
            bytte = True
    if bytte == False:
        break
    
print(liste)
print()