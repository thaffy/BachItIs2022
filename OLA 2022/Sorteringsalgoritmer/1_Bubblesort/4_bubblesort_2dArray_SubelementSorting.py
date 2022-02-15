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