# To variable for å holde orden på minste tall og tallnr, begges settes lik 0
minst=0
tallnr=0

# Fem vilkårlige tall som inndata
t1=int(input('Oppgi tall nr 1: '))
t2=int(input('Oppgi tall nr 2: '))
t3=int(input('Oppgi tall nr 3: '))
t4=int(input('Oppgi tall nr 4: '))
t5=int(input('Oppgi tall nr 5: '))

if t1>t2:
    minst=t2
    tallnr=2
else:
    minst=t1
    tallnr=1

if minst>t3:
    minst=t3
    tallnr=3

if minst>t4:
    minst=t4
    tallnr=4

if minst>t5:
    minst=t5
    tallnr=5

# Skriver ut resultatet, minste tall og tallnr
print('Det minste tallet er',minst,' og det er tallnr',tallnr,'i rekka.')
    
