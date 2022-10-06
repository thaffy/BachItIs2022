def main():

    # Løkkevariabler
    run = True
    while run == True:
        print()

        ### Input ###
        mndForbruk = int(input("Antall kilowatt-timer: "))
        kwtPris = int(input("Pris per kilowatt-time i øre: "))
        basisSum = (mndForbruk * (kwtPris/100))

        ### Beregninger ###
        if kwtPris > 70:
            if mndForbruk > 5000:
                statsStotte = (5000 * ((kwtPris-70)/100)) * 0.9
            else:
                statsStotte = (mndForbruk * ((kwtPris-70)/100)) * 0.9
            totalSum = basisSum - statsStotte
        else:
            statsStotte = 0
            totalSum = mndForbruk * (kwtPris/100)

        ### Output ###
        print()
        print("BasisPris: ",basisSum)
        print("Statsstøtte: ",statsStotte)
        print("Totalsum:","{:.2f}".format(totalSum))
        print()

        ### Loop ###
        runAgain = input("Vil du kjøre programmet igjen? (j/n): ")
        if runAgain != "j" and runAgain != "J":
            run = False

if __name__ == "__main__":
    main()


