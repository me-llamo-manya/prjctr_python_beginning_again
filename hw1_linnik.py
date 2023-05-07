# 1. Write a program that gets two int variables and swaps their values. Do it in 3 different ways.
# a = 3b = 5# write your code here
# 1st way - by using the third variable:
a = int(input('Enter value for a: '))
b = int(input('Enter value for b: '))

c = a 
a = b 
b = c
print(a)
print(b)

# 2nd way - using tuple syntax
var1 = int(input('Enter value for first variable: '))
var2 = int(input('Enter value for second variable: '))

var1, var2 = var2, var1
print(var1)
print(var2)

# 3rd - by adding second variable value to the first and then substract it from the sum
int1 = int(input('Enter value for first int: '))
int2 = int(input('Enter value for second int: '))

int1 = int1 + int2
int2 = int1 - int2
int1 = int1 - int2
print(int1)
print(int2)

# 2. Write a program that gets 2 numbers from the user. Print to the console their difference.  
# Use the built-in Input function for that
# Enter the first digit: 5
# Enter the second digit: 3
# The difference is: 2

num1 = int(input('Enter the first digit: '))
num2 = int(input('Enter the second digit: '))
difference = abs(num1 - num2)
print('The difference is: ', difference)

#3. Write a program that gets 2 numbers from the user. Print to the console maximum of these two variable. Use a built-in function for that.
# Enter the first digit: 75
# Enter the second digit: 34
# The maximum is: 75

digit1 = int(input('Enter the first digit: '))
digit2 = int(input('Enter the second digit: '))
maximum = max(digit1, digit2)
print('The maximum is: ', maximum)

# Optional: Write a program that gets 3 digit number from the user and reverses it. 
# You can use only numbers and their operators. Don`t use a string here!
# Enter the initial number: 123
# The reverse number is: 321

initial_number = int(input('Enter the initial number: '))
ones = initial_number % 10
tens = (initial_number //10) % 10
hundreds = (initial_number//100) % 10
reverse_number = ones * 100 + tens *10 + hundreds
print('The reverse number is: ', reverse_number)