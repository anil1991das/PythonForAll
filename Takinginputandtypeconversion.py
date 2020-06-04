# num1 = 100
# num2 = 200
#
# print(num1+num2)    #300

# num1=input("enter first number:")
# num2=input("enter second number:")
# print(type(num1))
# print(type(num2))
# print(num1+num2)
""" here we see its just concatanation
class 'str'>
<class 'str'>  bcz its just string
enter first number:100
enter second number:200
100200
"""

#approach1
# If you want to perform a mathematical operation then need to convert to int.

# num1=int(input("enter first number:"))
# num2=int(input("enter second number:"))
# print(type(num1))
# print(type(num2))
# print(num1+num2)

#approach 2

# num1=float(input("enter first number:"))
# num2=float(input("enter second number:"))
# print(type(num1))
# print(type(num2))
# print(num1+num2)

#approach 3
num1=input("enter first number:")
num2=input("enter second number:")
print(int(num1)+int(num2))