les_inn='Ja'
navnliste=[]
antall_navn=0

while les_inn=='Ja' or les_inn=='j' or les_inn=='ja':
    fornavn=input('Oppgi et fornavn: ')
    navnliste +=[fornavn]
    antall_navn=antall_navn+1


    les_inn=input('Vil du skrive inn et nytt fornavn? ')
    
print('Her er lista over navn du har skrevet inn:')
print(navnliste)
print()
print('Her er lista reversert:')

for i in range(1,antall_navn+1,1):
    print(navnliste)
    n=navnliste[i]
    navnliste[i]=navnliste[i-antall_navn-1]
    navnliste[i-antall_navn-1]=n

print(navnliste)





# print('Antall navn skrevet inn = ',antall_navn)






    
