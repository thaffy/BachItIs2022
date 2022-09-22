from datetime import datetime

year = input('Skriv inn YYYYMMDD ')
dato_formatted = f'{year[:4]}-{year[4:6]}-{year[6:]}'
print(dato_formatted)

