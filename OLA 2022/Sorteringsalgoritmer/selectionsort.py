
liste = [1,5,4,7,12,78,67,54,3,2,55,43,32,13,14,1,90,87]
print(liste)
listelengde = len(liste)

for i in range(0,listelengde-1,1):
    min = i
    for j in range(i+1,listelengde,1):
        if liste[j] < liste[min]:
            min = j
    
    if min != i:
        k = liste[i]
        liste[i] = liste[min]
        liste[min] = k
        
print(liste)
