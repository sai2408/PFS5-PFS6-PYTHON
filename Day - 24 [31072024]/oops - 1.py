'''
class sai:
    def __init__(self):
        print("I am a constructor")
    a = 10
    b = 20
    def wopwor(self):
        print("I am WOPWOR")
    def wopwr(self):
        return "I am WOPWR"
    def wpwor(self,a,b):
        x = a+b
        print("I am WPWOR,",x)
    def wpwr(self,a,b):
        x = a*b
        res = "I am WPWR" + str(x)
        return res
ob1 = sai()
print(ob1.a)
print(ob1.b)
ob1.wopwor()
print(ob1.wopwr())
ob1.wpwor(10,20)
a = ob1.wpwr(2,5)
print(a)
x1 = sai()
x2 = sai()
x1.wpwor(2,5)
x2.wpwor(5,5)
x1 = sai()
x2 = sai()
'''
'''
class sai1:
    def __init__(self,a,b):
        print(a+b)
x1 = sai1(10,20)
x2 = sai1(100,200)
'''
'''
class xyz:
    def __init__(self,a,b):
        print(a+b)
n1 = 30
n2 = 40
x1 = xyz(n1,n2)
'''
class details:
    def __init__(self):
        self.name = input("enter Your Name : ")
        self.mobile = int(input("enter Your Mobile Number : "))
    def display1(self):
        print("My name is :",self.name)
    def display2(self):
        print("My Mobile number is :",self.mobile)
ob1 = details()
ob1.display1()
ob2 = details()
ob2.display1()
'''
class xyz:
    a = 10
    b = 20
    def __init__(self):
        print("I am constructor")
    def display(self,name):
        print("Hello",name)
x1 = xyz()
x1.display("Sai Vardhan")
'''









    










