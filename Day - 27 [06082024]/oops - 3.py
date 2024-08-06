#Multi level Inheritance
'''
class A:
    def fun1(self):
        print("I am from class a")
class B(A):
    def fun2(self):
        print("I am from class b")
class c(B):
    def fun3(self):
        print("I am from class c")
oc = c()
oc.fun3()
oc.fun2()
oc.fun1()
'''
#Hirarical Inheritance
'''
class A:
    def fun1(self):
        print("I am from class a")
class B(A):
    def fun2(self):
        print("I am from class b")
class C(A):
    def fun3(self):
        print("I am from class c")
oc = C()
oc.fun3()
oc.fun1()
ob = B()
ob.fun2()
ob.fun1()
'''
#Hybrid Inheritance
'''
class A:
    a = 10
class B(A):
    b = 20
class C(A):
    c = 30
class D(C):
    d = 40
od = D()
print(od.d)
print(od.c)
print(od.a)
print(od.b)
'''
#Problem
'''
class A:
    def abc(self):
        a = 10
        b = 20
        return a
class B(A):
    def xyx(self):
        print(self.abc())
ob = B()
ob.xyx()
'''
#Abstraction
'''
from abc import ABC,abstractmethod
class A(ABC):
    @abstractmethod
    def abc(self):
        print("I am abc")
    def xyz(self):
        print("I am xyz")
oa = A()
'''
#Exception Handling
#Example - 1
'''
try:
    a = 10
    b = "mnl"
    c = a + b
except:
    print("Error Occured")
else:
    print(c)
finally:
    print("I am Final Block")
'''
#Example - 2
'''
try:
    a = 10
    c = z
except ZeroDivisionError:
    print("Denominator should not be 0")
except TypeError:
    print("Type error occured")
except:
    print("Other Error Occured")
else:
    print(c)
finally:
    print("Finally Block")
'''
#Example - 3
'''
try:
    a = 10
    c = z
except ZeroDivisionError:
    print("Denominator should not be 0")
except TypeError:
    print("Type error occured")
except Exception as e:
    print(e)
else:
    print(c)
finally:
    print("Finally Block")
'''
















