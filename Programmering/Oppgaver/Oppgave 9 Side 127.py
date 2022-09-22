import math
# ^ Importerer verdien for pi, slik at man kan bruke math.pi i stedet for et tall.

#Spør bruker om inndata
user_circle_radius=int(input('Please input the radius of your circle: '))

#Bergner areal
sirkel_areal=math.pi*user_circle_radius**2 # ** betyr potens

#Beregner omkrets
sirkel_omkrets=2*math.pi*user_circle_radius


#Skriver ut areal og omkrets
print()
print('Arealet til sirkelen din er',sirkel_areal)
print('Omkretsen til sirkelen din er',sirkel_omkrets)



