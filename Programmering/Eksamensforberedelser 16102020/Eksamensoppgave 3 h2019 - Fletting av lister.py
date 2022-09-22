

l1 = [1,14,26,37,100,86,77,99]
l2 = [2,13,27,38,99,85,78,101,4,47,56]

nyliste=[]

print(l1)
print(l2)
print(nyliste)
print()

for n in range(0,8,1):
    nyliste +=[l1[n]]

for n in range(0,11,1):
    nyliste +=[l2[n]]

print('Ny liste: ',nyliste)
