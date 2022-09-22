# Første og siste element i en liste skal bytte plass.

tallliste=[5,3,2,1,4]
print('Lista før bytte er',tallliste)
print('Første og siste element i lista skal bytte plass.')
print()

# Bytte er byttevariabelen vi bruker for å ta vare på første verdi.
bytte=tallliste[0]

# Tallliste av 0 får verdien til tallliste av 4
tallliste[0]=tallliste[4]

# Tallliste av 4 får verdien som vi tok vare på i byttevariabelen
tallliste[4]=bytte

# Lista etter bytte er
print('Lista etter bytte er',tallliste)
