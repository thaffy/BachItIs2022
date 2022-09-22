
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

# Utvidelse av Forelesning19102020-3
# Forrige utskrift gir utskrift av lista
# Utskrift av alle navnene gjøres me en for-løkke

listelengde=len(fornavn)
for index in range(0,listelengde,1):
    print('Fornavn nr',index+1,'er',fornavn[index])

print()

# Utskrift av navnene i motsatt rekkefølge, fra siste til første
for index in range(listelengde-1,-1,-1):
    print('Fornavn nr',index+1,'er',fornavn[index])

    
    
