#A customer in a store is purchasing five different items.
#Write a program that asks for the price of each item, then displays the subtotal of the sale, the amount of sales tax, and the total.
#Assume the sales tax is 7 percent.

item1=float(input('Enter the price for your first item: '))
item2=float(input('Enter the price for your second item: '))
item3=float(input('Enter the price for your third item: '))
item4=float(input('Enter the price for your fourth item: '))
item5=float(input('Enter the price for your fifth item: '))

pre_tax_total=item1+item2+item3+item4+item5
tax='7 percent.'
after_tax_total=pre_tax_total*1.07


print('Your subtotal is',pre_tax_total)
print('The sales tax is',tax)
print('Your total is',after_tax_total,'after tax.')

       
