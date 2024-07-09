#List
#DEclaration
'''
x = [1,2,3,4]
print(x)
x = [1,2,3,"Sai",56.789]
print(x)
x = list(map(int,input()))
print(x)
x = list(map(int,input().split()))
print(x)
'''
#Accessing
#Indexing
#Postive Indexing
'''
x = [12,23,34,45,56]
print(x[1])
print(x[4])
print(x[8])
'''
#Negetive Indexing
'''
x = [12,23,34,45,56]
print(x[-1])
print(x[-4])
print(x[-8])
'''
#Looping
#For loop with range()
'''
x = [12,23,34,45,56,67]
for i in range(6):
    print(x[i],end="_")
print()
'''
#For loop without range()
'''
x = [12,23,34,45,56,67]
for i in x:
    print(i,end="_")
'''
#Kwargs
'''
x = [12,23,34,45,56,67]
print(x)
print(*x)
print(*x,sep=" ")
print(*x,sep="_")
'''



















