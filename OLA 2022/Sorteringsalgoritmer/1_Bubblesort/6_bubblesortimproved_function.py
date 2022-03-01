

def bubbleSort(array):
    n = len(array)
    for i in range(n-1): 
        swapped = False
        for j in range(0,n-i-1):
            if array[j] > array[j+1]:
                array[j],array[j + 1] = array[j + 1], array[j]
                swapped = True
        if swapped == False:
            break
    return array