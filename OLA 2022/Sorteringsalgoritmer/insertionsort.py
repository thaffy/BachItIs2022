

liste = [1,5,4,7,12,78,67,54,3,2,55,43,32,13,14,1,90,87]
listelengde = len(liste)
print(liste)

i = 1
while i < listelengde:
    j = i
    while j > 0 and liste[j-1] > liste[j]:
        k = liste[j]
        liste[j] = liste[j-1]
        liste[j-1] = k
        j -= 1
    i += 1

print(liste)