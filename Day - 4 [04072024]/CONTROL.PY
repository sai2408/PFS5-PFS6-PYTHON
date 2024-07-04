#For Loop
#=>Range - range(start,end,step)
'''
for i in range(3):
    print(i)
'''
'''
for i in range(10):
    print(i)
for i in range(0,3):
    print(i)
for  i in range(0,3,1):
    print(i)
for i in range(0,11,1):
    print(i)
for i in range(1,11):
    if i%2==0:
        print(i)
for i in range(1,11,4):
    print(i)
for i in range(5,0,-1):
    print(i)
for i in range(10,4,-1):
    print(i)
for i in range(-1,-6,-1):
    print(i)
for i in range(-5,0,1):
    print(i)
'''
#Traingle Validator
a,b,c = map(int,input().split())
if ((a+b>c) and (a+c>b) and (b+c>a)):
    print("Yes")
else:
    print("No")



























    

