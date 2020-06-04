# name= "John"
# age= 30
# sal=500000.50

name,age,sal="John",30,500000.50

#Approach 1

# print(name,age,sal)   #John 30 500000.5

#approach 2

# print("Name is:",name)
# print("Age is:",age)
# print("Salary is:",sal)

#Approach3
#Single line % operator

# print("Name: %s age=%d salary=%g" %(name,age,sal))   #Name: John age=30 salary=500000

#Approach 4
#single line {}

# print("Name:{} age:{} Salary:{}".format(name,age,sal))   #Name:John age:30 Salary:500000.5

#Approach 5

# print("Name:{0} age:{1} Salary:{2}".format(name,age,sal))  #Name:John age:30 Salary:500000.5
#
# print("Age:{1} Name:{0} Salary:{2}".format(name,age,sal))  # 0 1 2   Age:30 Name:John Salary:500000.5




