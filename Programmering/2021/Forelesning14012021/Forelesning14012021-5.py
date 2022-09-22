# Starter med en FOR-løkke som flytter største verdi til siste posisjon (en gjennomføring)

# "Sortering uten stopp-merke"

# Starter med en FOR-løkke som flytter største verdi til siste posisjon ( en gjennomføring)
usortert = [5,3,1,2,4,7,6]

print('Lista før sortering er:                              ',usortert)
print()
print()

antall_gjennomganger = 1
uten_bytte = 0
for n in range(0,len(usortert),1):
    for n in range(0,len(usortert)-1,1):
        if usortert[n] > usortert[n+1]:
            # Da skal de bytte plass
            bytte = usortert[n]
            usortert[n] = usortert[n+1]
            usortert[n+1] = bytte
            print('Resultat etter bytte nr',n+1,'i->',antall_gjennomganger,'<- gjennomgang er da,',usortert)

        print('Sammenligning uten bytter')

        uten_bytte = uten_bytte + 1
    antall_gjennomganger = antall_gjennomganger + 1


print()
# print('Da må vi starte en ny gjennomgang fra begynnelsen av lista')
print('Ferdig liste:',usortert)
print('Antall sammenligninger uten bytte ble',uten_bytte)
    
