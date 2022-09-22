#Write a program that asks the user to enter the amount of a purchase and the desired number of payment installments
#The program should add 5 percent to the amount to get the total purchase amount, and then devide it by the desired number of instalments
#then display messages telling the user the total amount of the purchase and how much each instalment will cost.

purchase_price=float(input('What is the total price for the product you are purchasing? '))
instalments=int(input('How many instalments would you like to divide the price into? '))

total_price=purchase_price*1.05
instalment_amount=purchase_price/instalments

print('The total amount of your purchase will be',total_price)
print('Each instalment will cost',instalment_amount)

