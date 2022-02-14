def partition(start,end,liste):
    pivot_index = start
    pivot = liste[pivot_index]

    while start < end:
        while start < len(liste) and liste[start] <= pivot:
            start += 1
        
        while liste[end] > pivot:
            end -= 1
        
        if end > start:
            liste[start],liste[end] = liste[end],liste[start]

    liste[end], liste[pivot_index] = liste[pivot_index], liste[end]
    return end

def quicksort(start,end,liste):
    if start < end:
        p = partition(start,end,liste)

        quicksort(start,p-1,liste)
        quicksort(p+1,end,liste)


liste = [1,5,4,7,12,78,67,54,3,2,55,43,32,13,14,1,90,87]
listelengde = len(liste)
print(liste)

quicksort(0,listelengde-1,liste)

print(liste)


