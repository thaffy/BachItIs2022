#Innstikksortering - v2021
#Program for å innstikksortere en usortert liste

#Pseudokode på algoritmen fra https://en.wikipedia.org/wiki/Insertion_sort

#for i ← 1 to length(A)
#    j ← i
#    while j > 0 and A[j-1] > A[j]
#        swap A[j] and A[j-1]
#        j ← j - 1
#    end while
#end for



usortert=[5,3,1,2,4]

tabellengde=len(usortert)
print(usortert)

for i in range(1,tabellengde,1):
    j=i

    while j>0 and usortert[j-1]>usortert[j]:
        x=usortert[j]
        usortert[j]=usortert[j-1]
        usortert[j-1]=x

        j=j-1

print(usortert)
