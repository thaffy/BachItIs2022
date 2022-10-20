print("loops")



for antall_km in range(1,6,1):
    tall = int(input("tall:"))
    pris1 = 750
    pris2 = 300 + (2 * antall_km)
    pris3 = 150 + (4 * antall_km)

    if pris1 > pris2:
        minstepris = pris2
    else:
        minstepris = pris1
    if minstepris > pris3:
        minstepris = pris3

    print("### Antall KM",antall_km,"###")
    print("Pris1:",pris1,"kr")
    print("Pris2:",pris2,"kr")
    print("Pris3:",pris3,"kr")
    print("Beste pris er...",minstepris)
    print()






