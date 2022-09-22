#Program for å beregne farge på ruletten

#Alternativ 3, tar utgangspunkt i hvilke farger som gjelder for hvilke intervaller og "talltype"

#1 test på farge, dvs sann/usann på if-test nr 3


#Brukeren oppgir verdi på ruletten
tall=int(input('Hva er tallet på ruletten? '))

#Tester om gyldig verdi og beregner riktig farge for gyldige verdier
print()
if tall>=0 and tall<=36:
    if tall==0:
        print('Tallet er markert "grønn" på ruletten')
    else:
        #Hele if-setningen deles over flere linjer, må da stå i ekstra ()
        if ((tall>=1 and tall<=10 and (tall%2)==0)
        or (tall>=11 and tall<=18 and (tall%2)!=0)
        or (tall>=19 and tall<=28 and (tall%2)==0)
        or (tall>=29 and tall<=36 and (tall%2)!=0)):
            print('Tallet er markert "svart" på ruletten')
        else:
            print('Tallet er markert "rød" på ruletten')

else:
    print('Du har ikke oppgitt en gyldig verdi på ruletten')

print('Program avsluttet')
