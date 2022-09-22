
def marginCalc():
    print('----')
    print('Margin Calculator')
    itemName = input('Item Name: ')
    itemBuy = int(input('Buy Price: '))
    itemSell = int(input('Sell price: '))
    itemLimit = int(input('Item Buy limit: '))

    itemProfit = (itemSell - itemBuy) * itemLimit
    investment = (itemBuy * itemLimit)
    roiCalc = ((itemSell * itemLimit) - (itemBuy * itemLimit)) / (itemBuy * itemLimit)
    roi = roiCalc * 100
    
    print('-----')
    print('Potential Profit for',itemName,':',itemProfit)
    print('Return on investment:',format(roi, '.2f'),'%')

marginCalc()





