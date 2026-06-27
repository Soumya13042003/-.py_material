# 1.Write a Python program that takes a user input and prints it.

name = input("Please enter your name: ")
print(f"Hello,{name}")

# 2.Write a Python program to check if a number is positive, negative, or zero.

number = float(input("Enter a number: "))
if number > 0:
    print("The number is positive")
elif number < 0:
    print("the numbe is negative")
else:
    print("the number is zero")

# 3.Write a Python program to find the largest of three numbers.

num1 = float(input("enter a number: "))
num2 = float(input("enter a number: "))
#num3 = float(input("enter a number: "))

if (num1>=num2) and (num1>=num3):
    largest = num1
elif (num2 >= num1) and (num2 >= num3):
    largest = num2
else:
    largest = num3

print(f"largest number is {largest}") 

# 4. Write a Python program to calculate the factorial of a number.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

num = int(input("enter a number: "))

print(f"Factorial number of: {num} is {factorial(num)}")

