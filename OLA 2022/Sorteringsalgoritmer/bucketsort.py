def insertionsort(liste):
    i = 1
    listelengde = len(liste)
    while i < listelengde:
        j = i
        while j > 0 and liste[j-1] > liste[j]:
            k = liste[j]
            liste[j] = liste[j-1]
            liste[j-1] = k
            j -= 1
        i += 1