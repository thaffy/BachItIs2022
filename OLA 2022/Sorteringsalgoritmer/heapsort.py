def heapify(liste,listelengde,i):
    storste_verdi = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < listelengde and liste[i] < liste[left]:
        storste_verdi = left
    
    if right < listelengde and liste[storste_verdi] < liste[right]:
        storste_verdi = right

    if storste_verdi != i:
        liste[i],liste[storste_verdi] = liste[storste_verdi],liste[i]
        heapify(liste,listelengde,storste_verdi)

def heapsort(liste):

    for i in range(listelengde // 2 - 1, -1, -1):
            heapify(liste, listelengde, i)

    for i in range(listelengde-1, 0, -1):
        liste[i], liste[0] = liste[0], liste[i]   
        heapify(liste, i, 0)


liste = [1,5,4,7,12,78,67,54,3,2,55,43,32,13,14,1,90,87]

print(liste) # <- Før sortering
print()
listelengde = len(liste)
heapsort(liste) # <- Sender til sortering
print()
print(liste) # <- Etter sortering


