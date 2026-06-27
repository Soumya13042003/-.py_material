# 1. Create variables of different data types: integer, float, string, and boolean. Print their values and types.

name = input("enter your name: ")
num1 = int(input("enter your number: "))
num2 = int(input("enter your number: "))

number = (num1 == num2)
print(name)
print(type(name))

print(num1, type(num1))
print(num2, type(num2))

print(number)
print(type(number))

# 2. Write a Python program to swap the values of two variables.

a = 5
b = 10

print(f"Before swap a: {a} and b: {b}")

a, b=b, a
print(f"After swap a: {a} and b: {b}")

# 3. Write a Python program to convert Celsius to Fahrenheit

celsius = float(input("enter tempature value: "))
fahrenheit = (celsius * 9/5) + 32
print(fahrenheit)

# 4. Write a Python program to concatenate two strings.

a = "Hello"
b = "world"

print(f"The word is {a +" "+ b}")

# 5. Write a Python program to check if a variable is of a specific data type.

num1 = 10
if isinstance(num1, int):
    print(f"{num1} is int")
else:
    print(f"{num1} is not int")