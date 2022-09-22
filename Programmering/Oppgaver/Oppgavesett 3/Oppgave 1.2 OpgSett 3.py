les_inn='Ja'
navnliste=[]
antall_navn=0

while les_inn=='Ja':
    fornavn=input('Oppgi et fornavn: ')
    navnliste +=[fornavn]
    antall_navn=antall_navn+1


    les_inn=input('Vil du skrive inn et nytt fornavn? ')

print('Her er lista over navn du har skrevet inn:')
print(navnliste)
print('Her er lista reversert:')
navnliste.reverse()
print(navnliste)




# print('Antall navn skrevet inn = ',antall_navn)






    
