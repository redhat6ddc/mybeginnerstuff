#python program to find the largest number out of the three numbers
global count
count=15

def largest(number1,number2,number3):
    global largest
    largest = number1
    if largest < number2:
        if number2 > number3:
            largest= number2
        else:
            largest = number3
    elif largest < number3:
        if number3 > number2:
            largest = number3
        else :
            largest = number2
    else :
        largest = number1



print('this program finds out the largest number out of the given three numbers')
print('enter x to exit')
number1= input('enter the first number : ')



    
if number1=='x' :
    print('you chose to exit the program')
    exit()
else :
    number1= int(number1)
    number2= int(input('enter the second number : '))
    number3= int(input('enter the third number : '))
    largest(number1,number2,number3)
    if largest == number2 and number2 == number3:
        count =0
    if count==0 :
        print('All The Three Numbers Are Equal To Each Other')
    else :
        print('The Largest Number Is : ' + str(largest) )
