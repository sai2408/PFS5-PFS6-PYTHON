#Built in functions
'''
print(abs(-10))
print(abs(10))
print(ord("a"))
print(ord("A"))
print(chr(97))
print(chr(65))
print(eval("10+20"))
print(eval("20%10"))
a = 10
print(id(a))
print(bin(10))
print(hex(34))
print(oct(16))
print(max(10,20,30))
print(min(10,20,30))
print(sum([10,20,30]))
'''
#User Defined Functions
#Way too long words
#Approach - 1[Normal Method]
'''
s = input()
if len(s) <= 10:
    print(s)
else:
    res = ""
    res = res + s[0]
    res = res + str(len(s)-2)
    res = res + s[-1]
    print(res)
'''
#Approach - 2 [WPWR]
'''
def fun1(s):
    if len(s)<=10:
        return s
    else:
        res = ""
        res = res + s[0]
        res = res + str(len(s)-2)
        res = res + s[-1]
        return res
t = int(input())
for i in range(t):
    x = input()
    print(fun1(x))
'''
#Approach - 3 [WPWOR]
'''
def fun1(s):
    if len(s)<=10:
        print(s)
    else:
        res = ""
        res = res + s[0]
        res = res + str(len(s)-2)
        res = res + s[-1]
        print(res)
t = int(input())
for i in range(t):
    x = input()
    fun1(x)
'''
#Approach - 4 [WOPWR]
'''
def fun1():
    s = input()
    if len(s)<=10:
        return s
    else:
        res = ""
        res = res + s[0]
        res = res + str(len(s)-2)
        res = res + s[-1]
        return res
t = int(input())
for i in range(t):
    print(fun1())
'''
#Approach - 5 [WOPWOR]
'''
def fun1():
    s = input()
    if len(s)<=10:
        print(s)
    else:
        res = ""
        res = res + s[0]
        res = res + str(len(s)-2)
        res = res + s[-1]
        print(res)
t = int(input())
for i in range(t):
    fun1()
'''
#Default Arguments
'''
def fun(a=10,b=20):
    print(a+b)
fun()
fun(20)
fun(100,200)
'''
#Required Arguments
'''
def fun(a,b):
    print(a+b)
#fun()
#fun(20)
fun(100,200)
'''
#Keywords arguments
'''
def fun(a=10,b=20):
    print(a+b)
fun()
fun(b=20)
'''
#Varibale number of arguments
'''
def fun(*x):
    res = 0
    for i in x:
        res = res + i
    print(res)
fun()
fun(1)
fun(1,2)
fun(1,2,3,4)
'''










































