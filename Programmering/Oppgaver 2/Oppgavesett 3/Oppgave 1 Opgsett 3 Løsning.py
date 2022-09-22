
fornavn=[]
nytt_navn=True

while nytt_navn==True:
    navn=input('Oppgi fornavn: ')
    fornavn +=[navn]

    svar=input('Skal det leses inn flere fornavn? (ja/nei) ')
    if svar=='nei':
        nytt_navn=False
        
print('Navnlisten du har skrevet inn er:')
print(fornavn)

listelengde=len(fornavn)
    
