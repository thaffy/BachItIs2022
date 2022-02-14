
def mergesort(liste):
    if len(liste) > 1:

        mid = len(liste)//2
        left = liste[:mid]
        right = liste[mid:]

        mergesort(left)
        mergesort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                liste[k] = left[i]
                i += 1
            else:
                liste[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            liste[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            liste[k] = right[j]
            j += 1
            k += 1

liste = [1,5,4,7,12,78,67,54,3,2,55,43,32,13,14,1,90,87]
listelengde = len(liste)
print(liste)

mergesort(liste)

print(liste)



