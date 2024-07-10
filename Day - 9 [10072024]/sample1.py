#List  Methods
'''
x = [10,"a"]
print(x)
#append()
x.append("d")
print(x)
x.append([1,2,3])
print(x)
#extend()
x.extend([1,2,3])
print(x)
#insert()
x = [1,2,4,5]
print(x)
x.insert(2,3)
print(x)
#remove()
x.remove(5)
print(x)
x = [10,20,30,20,40]
print(x)
x.remove(20)
print(x)
#pop()
x.pop()
print(x)
x.pop(1)
print(x)
#index()
x = [1,2,3,4,2,3,4,5]
print(x)
print(x.index(5))
print(x)
#clear()
x.clear()
print(x)
#copy()
a = [1,2,3,4,5]
b = a.copy()
print(b)
#sort()
a = [45,1235,86,2,6,1,5]
a.sort()
print(a)
#reverse()
a.reverse()
print(a)
#count()
a = [2,5,2,6,1,7,2,6,2]
print(a)
print(a.count(2))
'''
#List Built in Functions
'''
#sum()
a = [10,20]
print(sum(a))
#max()
a = [10,20,400,30]
print(max(a))
#min()
a = [10,20,400,30]
print(min(a))
#all()
a = [10,20,0,40]
print(all(a))
#any()
a = [0,0,0,0]
print(any(a))
#len()
a = [1,2,3,4,5]
print(len(a))
#sorted()
a = [34,1,4,1,45,3,6,2]
print(sorted(a))
'''
#slicing
'''
a = [1,2,3,4,5,6,7,8,9]
print(a)
print(a[:])
print(a[::])
print(a[::1])
print(a[0::1])
print(a[0:9:1])
print(a[5:])
print(a[3:7])
print(a[::3])
print(a[::-1])
print(a)
print(a[-3:-8:-1])
a = [4,6,23,90,24,9]
print(a)
'''
'''
s = 0
for i in a[::2]:
    if i%2 == 0:
        s = s + i
print(s)
'''
#Nested Lists
'''
row = int(input())
col = int(input())
matrix = []
for i in range(row):
    x = list(map(int,input().split()))[:col]
    matrix.append(x)
print(matrix)
for i in matrix:
    print(*i,sep=" ")
'''
#Duplicates
#Approach - 1
'''
n = int(input())
a = list(map(int,input().split()))[:n]
t = []
dup = []
for i in a:
    if i not in t:
        t.append(i)
    else:
        dup.append(i)
print(*dup)
'''
#Approach - 2
'''
n = int(input())
a = list(map(int,input().split()))[:n]
for i in a:
    if a.count(i)>1:
        print(i)
        break
'''
#Approach - 3
'''
n = int(input())
a = list(map(int,input().split()))[:n]
for i in range(n):
    if a[i] in a[i+1:]:
        print(a[i])
        break
'''
    















































