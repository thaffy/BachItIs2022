#Assuming there is no accidents or delays, the distance that a car travels down the interstate can be calculated with the following formula: Distance = Speed x Time
#A car is travelling at 70 miles per hour.
#Write a program that displays the following:
# * The distance the car will travel in 6 hours
# * The distance the car will travel in 10 hours
# * The distance the car will travel in 15 hours

speed=70
distance1=speed*6
distance2=speed*10
distance3=speed*15


print('A car travelling at 70 miles per hour will travel',distance1,'miles in 6 hours. ')
print('A car travelling at 70 miles per hour will travel',distance2,'miles in 10 hours. ')
print('A car travelling at 70 miles per hour will travel',distance3,'miles in 15 hours. ')

#EKSTRA FOR MORRO SKYLD - USER INPUT OG KALKULERING
user_speed=int(input('How many miles per hour is your car travelling at? '))
user_hours=int(input('How many hours will you be driving? '))

user_distance=user_speed*user_hours

print('You will travel',user_distance,'miles in',user_hours,'hours driving at',user_speed,'miles per hour. ')
#EKSTRA OVER







      

