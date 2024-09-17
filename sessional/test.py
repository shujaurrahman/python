# Get element using list comprehension
# numbers=[int(input(f"Enter number {i+1}: ")) for i in range(5)]
# print(*numbers)

# Program to read five real numbers and find the average and standard deviation:

# import math
# numbers=[]

# for i in range(5):
#     n=int(input("Enter element: "))
#     numbers.append(n)

# avg=sum(numbers)/len(numbers)
# v=sum((x-avg)**2 for x in numbers)/len(numbers)

# sd=math.sqrt(v)

# print(f"The avf is {avg}")
# print(f"The variance is {v}")
# print(f"The sd is {sd}")

# Program to compute the value of an algebraic expression:

# x = float(input("Enter the value of x: "))
# y = float(input("Enter the value of y: "))

# result = 1 + (x/y) + (x*y) + 2 + (y/x) + (y*x)
# print(f"Result: {result}")

# Program to multiply an integer by 2 using the bitwise operator:

# n=int(input("Enter a number: "))

# r=n<<1
# print(f"Result: {r}")


# Program to divide an integer by 4 using the bitwise operator:

# n=int(input("Enter a number: "))

# r=n>>2
# print(f"Result: {r}")


# Program to exchange values of two variables using bitwise XOR operator:

# a=int(input("Enter first number: "))
# b=int(input("Enter first number: "))

# print(f"before reversing a and b  {a}  {b}")

# a=a^b
# b=a^b
# a=a^b

# print(f"after reversing a and b  {a}  {b}")


# Program to exchange values of two variables using addition and subtraction:

# a=int(input("Enter first number: "))
# b=int(input("Enter first number: "))

# print(f"before reversing a and b  {a}  {b}")

# a=a+b
# b=a-b
# a=a-b

# print(f"after reversing a and b  {a}  {b}")

# Program to check if an integer is even or odd using bitwise operator:

# n=int(input("Enter a number: "))
# if n&1:
#     print("odd")
# else:
#     print("even") 

# Program to find the maximum of three numbers:

# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))
# c = int(input("Enter the third number: "))

# max_num = max(a, b, c)
# print(f"The maximum number is: {max_num}")


# Program to find the distance between two points on an x-y plane:

# import math

# x1,y1=map(int,input("Enter first coordinates: ").split(","))
# x2,y2=map(int,input("Enter second coordinates: ").split(","))

# distance=math.sqrt((x2-x1)**2+(y2-y1)**2)

# print(f"result {distance}")


# Program to compute the factorial of an integer:

# def fact(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*fact(n-1)
    
# n=int(input("Enter a number : "))
# f=fact(n)
# print(f"result:  {f}")


# Program to check whether an integer is prime:

# def is_prime(n):
#     if n<2:
#         return False
#     for i in range(2,int(n**0.5)+1):
#         if n%i==0:
#             return False
#     return True
    


# x=int(input("Enter a number : "))

# if is_prime(x):
#     print("Prime ")
# else:
#     print("Not prime")


# Program to find prime numbers between two numbers:

# def is_prime(n):
#     if n<2:
#         return False
#     for i in range(2,int(n**0.5)+1):
#         if n%i==0:
#             return False
#     return True

# start=int(input("Enter starting number: "))
# end=int(input("Enter starting number: "))

# for i in range(start,end):
#     if is_prime(i):
#         print(i)
    

# Python function to calculate the sum of digits of a given integer:

# def sum_digit(n):
#     return sum(int(digit) for digit in str(n))

# n=int(input("Enter a number: "))
# print(f"result : {sum_digit(n)}")


# Function to add arbitrary integers:

# def add(*arg):
#     return sum(arg)

# n=int(input("how many numbers: "))
# # list=[]
# # for i in range(n):
# #     x=int(input("Enter numner: "))
# #     list.append(x)

# list=[int(input(f"Enter number {i+1}")) for i in range(n)]
# print(f"result : {add(*list)}")

