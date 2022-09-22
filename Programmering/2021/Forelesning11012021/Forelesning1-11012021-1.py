studentfil = open ('studentoblig99.txt','r')

#... her kommmer den vanlige koden....,
# eksemplifisert med enkel innlesning og utskrift av innholdet på studentfila

alle_studenter = studentfil.read()
print(alle_studenter)
studentfil.close()
