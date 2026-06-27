# 1. Write a Python program to perform arithmetic operations: addition, subtraction, multiplication, and division.
num1 = 12
num2 = 12

print(f"Addition: {num1 + num2}")
print(f"Substraction: {num1 - num2}")
print(f"Multiplication: {num1 * num2}")
print(f"Division: {num1 / num2}")

# 2. Write a Python program to demonstrate comparison operators: equal to, not equal to, greater than, less than.

num1 = 12
num2 = 12

print(f"Equal to {num1 == num2}")
print(f"not equal to {num1 != num2}")
print(f"greater than {num1 > num2}")
print(f"less than : {num1 < num2}")

# 3. Write a Python program to demonstrate logical operators: and, or, not

a = 0
b = 1

print(f"0 and 1 {a and b}")
print(f"0 and 1 {a or b}")
print(f"0 and 1 {not b}")

# 4. Write a Python program to calculate the square of a number.

a = float(input("enter a number: "))

power = a ** 2
print(f"The numer is {a} and power value {power}")

# 5. Write a Python program to check if a number is even or odd.
num = float(input("enter any number: "))
if num % 2 == 0:
    print(f"the {num} is even.")
else:
    print(f"the {num} is odd.")

# 6. Write a Python program to find the sum of the first n natural numbers.

n= float(input("enter any number: "))
num_1 = (n * (n+1)) // 2
print(f"the number is {n} and the value is {num_1}")

# 7. Write a Python program to check if a year is a leap year.

a = int(input("enter year: "))
if (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0):
    print(f"The {a} year is leap year")
else:
    print(f"The {a} year is not leap year")

# 8. Write a Python program to reverse a string.

string = input("enter a number: ")
reversed_string = string[::-1]
print(f"the string value {reversed_string}")

# 9. Write a Python program to check if a string is a palindrome.

string = input("enter number: ")
if string == string[::-1]:
    print(f"the {string} is palindrome.")
else:
    print(f"the {string} is not palindrome.")

# 10. Write a Python program to sort a list of numbers in ascending order.

num = [int(x) for x in (input("enter number is : ")).split()]
num.sort()
print(f"sorted list{num}")


