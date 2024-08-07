import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
class person:
    def __init__(self,name,age,email):
        self.name = name
        self.age = age
        self.email = email
class student(person):
    def __init__(self,name,age,email,roll,branch):
        super().__init__(name,age,email)
        self.roll = roll
        self.branch = branch
class teacher(person):
    def __init__(self,name,age,email,subject):
        super().__init__(name,age,email)
        self.subject = subject
class college:
    def __init__(self,name):
        self.name = name
        self.students = []
        self.teachers = []
    def add_student(self,student):
        self.students.append(student)
    def add_teacher(self,teacher):
        self.teachers.append(teacher)
    def display_students(self):
        if len(self.students) == 0:
            print("No students to this college")
        else:
            for i in self.students:
                print("Roll number:",i.roll)
                print("Name:",i.name)
                print("Branch:",i.branch)
    def display_teachers(self):
        if len(self.teachers) == 0:
            print("No teachers to this college")
        else:
            for i in self.teachers:
                print("Name:",i.name)
                print("Subject:",i.subject)
        
colleges = []
while True:
    print("Choose Option: ")
    print("1. To create College")
    print("2. To create Student")
    print("3. To Create Teacher")
    print("4. To print Students")
    print("5. To print Teachers")
    x = int(input())
    if x == 1:
        clg_name = input("Enter  College Name: ")
        x = False
        for i in colleges:
            if i.name == clg_name:
                x = True
                break
        if x == True:
            print("College Already Exits!")
        else:
            clg = college(clg_name)
            colleges.append(clg)
            print("College Created")
    elif x == 2:
        clg_name = input("Which College Student Belongs to ? \n")
        x = False
        for i in colleges:
            if i.name == clg_name:
                x = True
                y = i
                break
        if x == False:
            print("College Does not Exist!")
        else:
            roll = int(input("Enter Roll Number: "))
            name = input("enter Name of the student: ")
            age = int(input("Enter age of student: "))
            email = input("Enter email: ")
            branch = input("Enter Branch: ")
            s1 = student(name,age,email,roll,branch)
            y.add_student(s1)
    elif x == 3:
        clg_name = input("Which College Teacher Belongs to ? \n")
        x = False
        for i in colleges:
            if i.name == clg_name:
                x = True
                y = i
                break
        if x == False:
            print("College Does not Exist!")
        else:
            name = input("enter Name of the student: ")
            age = int(input("Enter age of student: "))
            email = input("Enter email: ")
            subject = input("Enter Subject: ")
            t1 = teacher(name,age,email,subject)
            y.add_teacher(t1)
    elif x == 4:
        clg_name = input("Which College students details do you want ?")
        x = False
        for i in colleges:
            if i.name == clg_name:
                x = True
                y = i
                break
        if x == False:
            print("College Does not Exist!")
        else:
            y.display_students()
    elif x == 5:
        clg_name = input("Which College teachers details do you want ?")
        x = False
        for i in colleges:
            if i.name == clg_name:
                x = True
                y = i
                break
        if x == False:
            print("College Does not Exist!")
        else:
            y.display_teachers()
            
'''
s1 = student("sai",26,"saivardhan.thimmisetty@gmail.com",101,"ece")
s2 = student("sai",26,"saivardhan.thimmisetty@gmail.com",101,"ece")

clg.add_student(s1)
clg.add_student(s2)

clg.display_students()
'''

        
