#Recursion - 1
'''
def calc(n):
    if n >= 1:
        print(n)
        calc(n-1)
calc(10)
'''
#Recursion - 2
'''
import sys
sys.setrecursionlimit(2000)
def calc(n):
    print(n)
    calc(n+1)
calc(1)
'''
#Recursion - 3
#While Loop
'''
n = int(input())
while n > 1:
    if n%2 == 0:
        print(n)
    n = n - 1
'''
#Recursion
'''
def name(n):
    if n > 1:
        if n%2 == 0:
            print(n)
        name(n-1)
    else:
        return
name(10)
'''
#Recursion - 4
#While
'''
n = int(input())
x = 1
while x <= n:
    print(x)
    x = x + 1
'''
#Recusrion
'''
def xyz(n,k):
    if k <= n:
        print(k)
    else:
        return
    xyz(n,k+1)
xyz(10,1)
'''
#Recursion - 5
#Factorial Value
'''
def fact(n):
    if n==1:
        return 1
    else:
        return n * fact(n-1)
print(fact(5))
'''
#Recursion - 6
#While Loop
'''
t = int(input())
while t > 0:
    x = int(input())
    if x%2 == 0:
        print("even")
    else:
        print("Odd")
    t = t - 1
'''
#Recursion - 1
'''
def recr(t):
    if t == 0:
        return
    else:
        n = int(input())
        evenorodd(n)
    recr(t-1)
def evenorodd(n):
    if n%2==0:
        print("Even")
    else:
        print("Odd")
t = int(input())
recr(t)
'''
#Recursion - 2
'''
def recr(t):
    if t == 0:
        return
    else:
        n = int(input())
        if n%2==0:
            print("Even")
        else:
            print("Odd")
    recr(t-1)

t = int(input())
recr(t)
'''



    














    











    


















    
        
        
