l1 = [1,5,8,18,19,23,54]
l2 = [77,6,9,13,14,33,49,67,88]
nyliste = []
nyliste2 = []
nyliste3 = []

print(l1)
print(l2)
print()

l1_lengde = len(l1)
l2_lengde = len(l2)
totallengde = l1_lengde + l2_lengde

print('Antall elementer i liste 1:',l1_lengde)
print('Antall elementer i liste 2:',l2_lengde)
print('Antall elementer totalt:',totallengde)
print()

# Enkeltvis innlegging med fletting av listene. Første element fra l1 blir lagt inn, deretter første element fra l2, deretter andre element fra l1 og andre element fra l2 osv
for n in range(totallengde):
    if n < l1_lengde:
        nyliste += [l1[n]]
    if n < l2_lengde:
        nyliste += [l2[n]]
print('Flettet liste:',nyliste)

# Enkeltvis innlegging uten fletting. Hele l1 blir lagt inn først, så hele l2
for n in range(l1_lengde):
    nyliste2 += [l1[n]]
for n in range(l2_lengde):
    nyliste2 += [l2[n]]
print('Sammenslått liste:',nyliste2)




    


        
    
    
