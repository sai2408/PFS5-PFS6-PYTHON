#Reverse of the Number
'''
n = int(input())
x = 0
if(n>=0):
    while n>0:
        r = n%10
        x = (x*10)+r
        n = n // 10
    print(x)
else:
    n = -1 * n
    while n>0:
        r = n%10
        x = (x*10)+r
        n = n // 10
    print(-1*x)
'''
#Second Largest
'''
a = int(input())
b = int(input())
c = int(input())
if (a>b and a>c):
    a = 0
elif b>a and b>c:
    b = 0
else:
    c = 0
if (a>b and a>c):
    print(a)
elif b>a and b>c:
    print(b)
else:
    print(c)
'''
#Watching Movie
'''
x = int(input())
y = int(input())
c = y//2
print(x-c)
'''
#Swapping
'''
a = int(input())
b = int(input())
a,b = b,a
print(a)
print(b)
'''
#Adding before and After
'''
n = int(input())
x = int(input())
n = (n*10)+x
res = 0
while (n>0):
    r = n%10
    res = (res*10)+r
    n = n // 10
res = (res*10)+x
res1 = 0
while(res>0):
    r = res%10
    res1 = (res1*10)+r
    res = res//10
print(res1)
'''
#Decomposition of a number
'''
n = int(input())
res = 0
if n>=0:
    while(n>0):
        r = n%10
        res= (res*10)+r
        n = n//10
    while res>0:
        r = res%10
        print(r)
        res = res//10
else:
    n = -1*n
    while (n>0):
        r = n%10
        res= (res*10)+r
        n = n//10
    while res>0:
        r = res%10
        print(r)
        res = res//10
'''
#Upcoming even number
'''
n = int(input())
if n%2 == 0:
    print(n+2)
else:
    print(n+1)
'''
#Helping chef
'''
n = int(input())
for i in range(n):
    x = int(input())
    if x < 10:
        print("Thanks for helping Chef !")
    else:
        print("-1")
'''
#discount
'''
n = int(input())
for i in range(n):
    x = int(input())
    print(100-)
'''
#Purchase Tv
n = int(input())
for i in range(n):
    a,b,c,d = map(int,input().split())
    fpa = a-c
    fpb = b-d
    if fpa < fpb:
        print("First")
    elif fpb < fpa:
        print("Second")
    else:
        print("Any")











    



























    
    
