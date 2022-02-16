#Ivan Barajas
#02.06.2022

#Problem 1
#Write a program that prints “Hello World” to the screen
print("Hello World")



#Problem 2
#Write a program that asks the user for their name and greets them with their name.
name = input ('What is your name?')
print("Hello," , name) 


#Problem 3
#Modify the previous program such that only the users you and your instructor are 
#greeted with their names. 
 

if name == 'Ivan':
    print('welcome, student')
elif name == 'Zoe':
    print('Welcome, professor')
    

#Problem 4
#Write a program that will compute the area of a circle. Prompt the user to enter 
#the radius and print a nice message back to the user with the answer
    
PI = 3.14
r = float(input("Enter the radius of the circle:"))
area = PI * r * r
print("Area of a circle = %.2f" %area)

#Problem 5
#Write a program that will compute MPG for a car. Prompt the user to enter the 
#number of miles driven and the number of gallons used.

milesDriven = float(input('Enter number of miles driven: '))
gallonsUsed = float(input('Enter gallons of gas used: '))

mpg = milesDriven / gallonsUsed

print('Miles per gallon =', mpg)

#Problem 6
#Write a program that will convert degrees Fahrenheit to degrees Celsius

temp = float(input("Enter temperature in Fahrenheit: "))

celsius = (temp - 32) * 5/9

print(f"{temp} in Fahrenheit is equal to {celsius} in Celsius")

#Problem 7
#Write a general version of the program which asks for the starting day number, and the length of your stay, and
#it will tell you the number of day of the week you will return on.
vacationStart=int(input('What day does your vacation start? (Enter 0 for Sunday, 1 for monday, etc.) '))

vacationLength=int(input('How many days will your vacation be? '))

returnDay=(vacationLength+vacationStart)%7

print('You will be back on day:', returnDay)
