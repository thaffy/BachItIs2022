### Lister ###

### 1.0 - Oppretting (definering) av en liste ###

# Oppretting av en tom liste
liste = []

# Oppretting av en liste med elementer
liste2 = ['Første','Andre','Tredje','Fjerde'] # <- Hvis elementene i listen er tekst (String) må vi ha '' rundt hvert element.
liste3 = [1,2,3,4,5,6,7,8,9,10] # <- Hvis elemtene i listen er tall eller variabler slipper vi å bruke ''





### 2.0 - Innskriving i lister ###
# Vi kan legge til element i en eksisterende liste med += eller ved å skrive liste = liste + [listeelement]
liste = liste + [1]
liste2 += ['Femte']
liste3 += [11]








### 3.0 - Utskrift av lister ###
# Vi kan skrive ut hele lister ved å skrive ut listevariabelen:
print(liste)
print(liste2)
print(liste3)

# For å hente ut ètt enkelt element bruker vi følgende skrivemåte: liste[n] hvor n er plassen i lista elementet er på
# Hvis vi bruker listen under som eksempel. Legg merke til kommentaren direkte over listen

#           [0]       [1]     [2]     [3]
liste4 = ['Første','Andre','Tredje','Fjerde'] 

# Hvis vi nå har lyst å skrive ut ordet "Tredje", som er på listeplass 2 så gjør vi følgende:
print(liste4[2]) # <- Legg merke til at ordet "Tredje" er element nr 3 i lista, men vi begynner å teller fra 0.
                 # <- Derfor må vi bruke [2] i stedet for [3] hvis vi vil ha element nr 3 i lista!




### 4.0 - 2-Dimensjonale Lister ###



