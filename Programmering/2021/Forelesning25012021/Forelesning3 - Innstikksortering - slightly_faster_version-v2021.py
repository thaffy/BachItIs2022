#Innstikksortering - slightly_faster_version-v2021
#Program for å innstikksortere en usortert liste

#fra https://en.wikipedia.org/wiki/Insertion_sort:
#kommentaren tar utgangspunkt i "Innstikksortering - v2021"
#After expanding the "swap" operation in-place as
#t ← A[j]; A[j] ← A[j-1]; A[j-1] ← t
#(where t is a temporary variable),
#a slightly faster version can be produced that moves A[i] to its position in one go
#and only performs one assignment in the inner loop body

#Pseudokoden blir da:
#for i = 1 to length(A)
#    x = A[i]
#    j = i - 1
#    while j >= 0 and A[j] > x
#        A[j+1] = A[j]
#        j = j - 1
#    end while
#    A[j+1] = x
# end for



usortert=[5,3,1,2,4]

tabellengde=len(usortert)
print(usortert)

for i in range(1,tabellengde,1):
    x=usortert[i]
    j=i-1
    
    while j>=0 and usortert[j]>x:
        usortert[j+1]=usortert[j]
        j=j-1
        
    usortert[j+1]=x
       
print(usortert)    

#The new inner loop shifts elements to the right to clear a spot for x = A[i]
