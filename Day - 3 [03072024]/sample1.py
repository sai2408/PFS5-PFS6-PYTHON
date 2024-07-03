print("Hello")
#Case - 1
'''
name = input("Enter Your Name: ")
age = int(input("enter Your age: "))
print(name)
print(age)
#Method 1
print("My name is",name,".",age,"is my age")
#Method 2[.format]
print("My name is {}. {} is my age".format(name,age))
#Method 3[f-format]
print(f"My name is {name}. {age} is my age")
'''
#Case - 2
b = 12.34567
print("The number is {:.10f}".format(b))
print(f"The number is {b}")

#Task
'''
Enter Your name[fname-lname]: Sai-T
Enter Your Height: 5-7
Enter Your Age: 30
Enter Your Salary: 50000
First name: Sai
Last name: T
Height: 5.7
Age: 30
Salary: 50000.00/-
'''
'''
fname,lname = input("Enter Your name[fname-lname]: ").split("-")
height1,height2 = input("Enter Your Height: ").split("-")
age = int(input("Enter Your Age: "))
salary = float(input("Enter Your Salary: "))
print("First name: {}".format(fname))
print("Last name: {}".format(lname))
print(f"Height: {height1+"."+height2}")
print("Age:",age)
print("Salary {:.2f}/-".format(salary))
'''



















