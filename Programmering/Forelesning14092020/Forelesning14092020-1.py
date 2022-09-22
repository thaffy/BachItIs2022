#Matematiske operatorer og operatorpresedens
#2.19 side 87

a=6+3*5
print('Svaret i a) er:',a)

b=12/2-4
print('Svaret i b) er:',b)

c=9+14*2-6
print('Svaret i c) er:',c)

d=(6+2)*3
print('Svaret i d) er:',d)

e=14/(11-4)
print('Svaret i e) er:',e)

f=9+12*(8-3)
print('Svaret i f) er:',f)


#Formatering av desimaltall
pris_pr_kg=10.37
antall_kg=9.6
totalpris=antall_kg*pris_pr_kg

print('Totalpris er:',totalpris)


dobbel_total=2*totalpris
print('Dobbel av totalpris er:',dobbel_total)

#Utskrift av totalpris avrundet til 2 desimaler
print('Totalpris er:',format(totalpris,'.2f'))
