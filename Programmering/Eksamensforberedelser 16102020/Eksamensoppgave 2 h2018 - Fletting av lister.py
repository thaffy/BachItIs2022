
#11 og 12 defineres med 7 elementer hver, nyliste defineres som en tom liste
l1 = [1,14,26,37,100,86,77]
l2 = [2,13,27,38,99,85,78]
nyliste = []

print(l1)
print(l2)
print(nyliste)
print()



for n in range(0,7,1):

    if l1[n] <= l2[n]:
        nyliste+=[l1[n]]
        nyliste+=[l2[n]]

    else:
        nyliste+=[l2[n]]
        nyliste+=[l1[n]]

print(nyliste)
        
