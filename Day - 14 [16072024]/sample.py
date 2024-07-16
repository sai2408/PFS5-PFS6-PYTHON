#Dictionary
#Creating of dictionary
'''
d = {1:10,2:20,3:30}
print(d)
d = {}
print(d)
d = {}
for i in range(3):
    x,y = map(int,input().split())
    d[x] = y
print(d)
'''
#Accessing of elements
'''
d = {1:10,2:20,3:30,4:40,5:50}
print(d[3])
print(d.get(3))
print(d.get(30))
for i in d:
    print(i,d[i])
'''
#Modify Dictionary
'''
d = {1:10,2:20,3:30}
d[2] = 200
print(d)
'''
#Insertion into Dictionary
'''
d = {1:10,2:20,3:30}
d[4] = 40
print(d)
'''
#Deletion of Dictionary
'''
d = {1:10,2:20,3:350,4:40}
del d[3]
print(d)
del d
print(d)
'''
#Methods in Dictionary
'''
#get()
d = {1:10,2:20,3:30}
print(d.get(2))
#update()
d = {1:10,2:20,3:30}
d1 = {2:250,4:40}
d.update(d1)
print(d)
#copy()
d = {1:20,2:20,3:30}
d1 = d.copy()
print(d1)
#pop()
d = {1:10,2:20,3:30,4:40}
d.pop(3)
print(d)
#popitem()
d = {1:10,2:20,3:30,4:40}
d.popitem()
print(d)
#clear()
d = {1:10,2:20,3:30,4:40}
d.clear()
print(d)
#keys()
d = {1:10,2:20,3:30,4:40}
print(d.keys())
#values()
d = {1:10,2:20,3:30,4:40}
print(d.values())
#items()
d = {1:10,2:20,3:30}
print(d.items())
#fromkeys()
s = {1,2,3,4}
print(s)
d1 = d.fromkeys(s,10)
print(d1)
#setdefault()
d = {1:10,2:20,3:30,4:40}
print(d.setdefault(1))
print(d)
print(d.setdefault(5))
print(d)
print(d.setdefault(6,60))
print(d)
'''
#Sample Program (Pangram/not)
s = "qwertyuiopasdfghjklzxcvbnm"
s1 = "qwertyuiopasdfghjklzxcvbnm"
d = {}
for i in s:
    if i in s1:
        if i not in d:
            d[i] = 1
if len(d) == 26:
    print("Pangram")
else:
    print("Not a pangram")

        




























