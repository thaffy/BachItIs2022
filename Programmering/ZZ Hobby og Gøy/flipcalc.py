

def addItem():

    # Cash stack for calculations
    print('-----')
    print('Add & Edit items')
    print('-----')
    cashStack = int(input('Current cash: ? '))
    print('-----')

    fliplist = open('fliplist.txt','a')

    # Info about item bought
    itemName = input('Input item name: ')
    buyPrice = int(input('Input buy price: '))
    sellPrice = int(input('Input sell price: '))
    itemLimit = int(input('Input item limit: '))


    # Calculations of profit based on cash stack and item limit
    margin = sellPrice - buyPrice
    amountBuyable = cashStack % buyPrice

    if amountBuyable >= itemLimit:
        profit = itemLimit * margin
        amountBuyable = itemLimit
        print('Itemlimit test')
    else:
        profit = amountBuyable * margin


    print('Margin = ',margin,'pr item.')
    print('-----')
    print('You can buy:',amountBuyable)
    print('Profit:',profit,'gp')
    print('-----')

#addItem()

def splitProfit():

    playerOneCash = int(input('Input first cashstack: '))
    playerTwoCash = int(input('Input second cashstack: '))

    if playerOneCash > playerTwoCash:
        split = playerTwoCash / playerOneCash
        percentageSplit = split * 100
        print(percentageSplit)
    else:
        split = playerOneCash / playerTwoCash
        percentageSplit = split * 100
        print(percentageSplit)

    endCash = int(input('How much cash do you want to split? '))

    print('Player One started with:',playeOneCash)
    print('Player Two started with:',playerTwoCash)
    print(


splitProfit()

    
                    
def main():

    pass main():
    run = True
    while run == True:
        print('-----')
        print('Please choose a module:')
        print('-----')
        print('1 - Add & Edit Items')
        print('2 - Combine cash & Split profits')
        print('0 - End session')
        print('-----')

        choice = int(input('Answer: '))

        if choice == 1:
            addItem()
        else:
            if choice == 2:
                splitProfit()
            else:
                run = False
                print('Session ended!')


main()
    

