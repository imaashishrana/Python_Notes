# """Python Notes
# This file is written like a simple study note for beginners.
# Each section explains a basic Python concept with comments.
# """

# # 1. Variables and data types
# # Python stores different kinds of values in variables.
# name = "Alice"          # string
# age = 20                # integer
# is_student = True       # boolean
# marks = [90, 85, 88]    # list

# print("Name:", name)
# print("Age:", age)
# print("Student:", is_student)
# print("Marks:", marks)

# # 2. Taking input from the user
# # input() reads text from the keyboard.
# user_name = input("Enter your name: ")
# user_age = int(input("Enter your age: "))

# print(f"Hello {user_name}, you are {user_age} years old.")

# # 3. Basic arithmetic operations
# # Python can do math using +, -, *, /, and **.
# a = 10
# b = 5

# print("Addition:", a + b)
# print("Subtraction:", a - b)
# print("Multiplication:", a * b)
# print("Division:", a / b)
# print("Power:", a ** 2)

# # 4. Conditional statements
# # if, elif, and else help us make decisions in the program.
# num = 100

# if 90 <= num <= 100:
#     grade = "A"
# elif 75 <= num < 90:
#     grade = "B"
# elif 60 <= num < 75:
#     grade = "C"
# else:
#     grade = "Fail"

# print("Grade:", grade)

# # 5. Simple notes for beginners
# # - Python uses indentation to define blocks of code.
# # - Use print() to display output.
# # - f-strings are useful for formatting text.
# # - Comments help explain code to readers and future learners.




# # a = False
# # # # print(type(a))

# # # a ={1,2,3,4,5,"hsj",1.2}

# # # print(type(a))


# # if a==True:
# #     print("hello")
# # else:print("Bye")


# # name = str(input())
# # age =int(input())

# # print(f"Age of  {name}  is { age} ")

# # print(type(name))
# # print(type(age))


# # a, b, c= map(int, input().split())

# # print(a)
# # print(b)
# # print(c)

# # arr= list(map(int, input().split()))


# # print(arr)


# # a= int(input())
# # b= int(input())

# # a, b = b, a

# # print(a)
# # print(b)


# # print("Hello, Python!")

# # name = input()

# # print(f"Welcome {name}")


# # a= int(input())
# # b= int(input())

# # print(a+b)

# # l= int(input())
# # b= int(input())

# # area = l*b

# # print(area)


# # a= int(input())

# # print(a**2)
# # print(a**3)

# # a= int(input())
# # b= int(input())
# # c = int(input())

# # print((a+b+c)/3)

# # a= int(input())
# # b= int(input())

# # a,b=b,a
# # print(a,b)

# # a= 1
# # b= 1.2
# # c="hello"
# # d=True
# # e={}

# # print(type(a))
# # print(type(b))
# # print(type(c))
# # print(type(d))
# # print(type(e))

# # r=int(input())
# # pi=3.14

# # area= pi*(r**2)
# # print(area)

# # celsius = 80
# # fa = (celsius* 9 / 5)+ 32
# # print(int(fa))



# #even or odd

# # num = int(input("Enter the number: "))

# # if num%2==0:
# #     print("even")
# # else:
# #     print("odd")


# # num =100

# # if num>=90 and num<=100:
# #     print("Grade A")
# # elif num >=75:
# #     print("Grade B")
# # elif num >=60:
# #     print("Grade C")
# # elif num >=50:
# #     print("Grade D")
# # else:
# #     print("Fail")


# #Check if a number is positive, negative, or zero.

# num = int(input("Enter a number: "))

# if num>0:
#     print("Positive")
# else:
#     if num<0:
#         print("Negative")
#     else:
#         print("Zero")


# Check whether a number is even or odd.

# num= int(input("Enter your NUmber:"))

# if num%2 == 0:
#     print("Even")
# else:
#     print("Odd")


# Find the largest of two numbers.

# num1= int(input("Enter your first number: "))
# num2= int(input("Enter your second number: "))

# if num1>num2:
#     print(f"{num1} is greater than {num2}")
# else:
#     print(f"{num2} is greater than {num1}")



# Find the largest of three numbers.

# num1 = int(input("Enter your first number: "))
# num2 = int(input("Enter your second number: "))
# num3 = int(input("Enter your third number: "))

# if num1>num2 and num1>num3:
#     print(f"{num1} is the largest number.")
# elif num2>num1 and num2>num3:
#     print(f"{num2} is the largest number.")
# else:
#     print(f"{num3} is the largest number.")

# Print numbers from 1 to 100.

# for i in range(1,101):
#     print(i)


# Print all even numbers from 1 to 100.

# for i in range(2,101,2):
#     print(i)

# # Print all odd numbers from 1 to 100.

# for i in range(1,101,2):
#     print(i)

# # Print numbers from 100 down to 1.

# for i in range(100,0,-1):
#     print(i)


# Find the sum of the first N numbers.

# num = int(input("Enter a number: "))
# sum =0 

# for i in range (1,num+1):
#     sum+=i
#     print(sum)

# Find the factorial of a number.\

# 4 = 1*2*3*4 factorial = 24 

# num = int(input("Enter a number: "))
# factorial =1
# for i in range(1,num+1):
#     factorial = factorial * i
# print(factorial)

# Count the number of digits in an integer.

# num = int(input("Enter a number : "))

# digit = 0
# if num == 0:
#     print("The number of digits is 1.")

# while num > 0:
#     num //= 10
#     digit +=1

# print(f"The number of digits is {digit}.")

# 1234 d=1
# 123  d=2
# 12   d=3
# 1    d=4




# Reverse an integer (e.g. 12345 → 54321).

# number = int(input("Enter a number: "))

# number = abs(number)  # Handle negative numbers

# reverse = 0

# while number > 0:
#     digit = number % 10
#     reverse = reverse * 10 + digit
#     number //=10

# if reverse < 0:
#     reverse = -reverse

# print(f"The reversed number is {reverse}.")

# Check if a number is a palindrome (e.g. 121).

# number = int(input("Enter a number: "))

# reverse = 0
# temp = number

# while temp > 0:
#     digit = temp % 10
#     reverse = reverse * 10 + digit
#     temp //=10

# if number == reverse:
#     print(f"{number} is a palindrome.")
# else:
#     print(f"{number} is not a palindrome.")

# Print the multiplication table for any number.


# number = int (input("Enter a number: "))

# for i in range(1,11):
#     print(f"{number} x {i} = {number*i}")



# Pattern Practice
# Square (4 × 4)

# for i in range (1,5):
#     for j in range(1,5):
#         print("*", end=" ")
#     print()  # Move to the next line after each row

# Right triangle

# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*", end=" ")
#     print()


# Inverted triangle

# for i in range(5,0,-1):
#     for j in range(1,i+1):
#         print("*", end=" ")
#     print()

# Pyramid of *

# for i in range(1,6):
#     print(" " * (5 - i), end="")  # Print leading spaces
#     print("* " * i)  # Print stars with a space

# # Floyd's Triangle

# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()  # Move to the next line after each row

# # Number triangle

# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print(i, end=" ")
#     print()  # Move to the next line after each row




