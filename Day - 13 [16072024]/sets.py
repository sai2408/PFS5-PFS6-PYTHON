#Creating Sets in Python
'''
s1 = {1,2,3,4}
print(s1)
s2 = {1,2,3,4,2,3,7}
print(s2)
s3 = {1,2,3.14,"python"}
print(s3)
s4 = set([1,2,3,4])
print(s4)
s5 = set(map(int,input().split()))
print(s5)
'''
#Accessing of Set elements
'''
s1 = {1,2,5,2,6,3,5}
for i in s1:
    print(i,end=" ")
'''
#Set methods
'''
s1 = {1,2,3,2,3,4}
print(s1)
'''
#add
'''
s1.add(10)
print(s1)
s1.add(2)
print(s1)
'''
#update
'''
s1 = {1,2,3,4}
s2 = {2,3,4,5}
print("Before Update")
print(s1)
print(s2)
s1.update(s2)
print("after Update")
print(s1)
print(s2)
'''
#copy
'''
s1 = {1,2,3,4}
s2 = {2,3,4,5}
print("Before Update")
print(s1)
print(s2)
s3 = s1.copy()
print(s3)
print("after Update")
print(s1)
print(s2)
'''
#clear
'''
s1 = {1,2,3,4}
s2 = {2,3,4,5}
print("Before Update")
print(s1)
print(s2)
s1.clear()
print("after Update")
print(s1)
print(s2)
'''
#remove
'''
s1 = {1,2,3,4}
s2 = {2,3,4,5}
print("Before Update")
print(s1)
print(s2)
s1.remove(2)
s2.remove(7)
print("after Update")
print(s1)
print(s2)
'''
#discard
'''
s1 = {1,2,3,4}
s2 = {2,3,4,5}
print("Before Update")
print(s1)
print(s2)
s1.discard(2)
s2.discard(7)
print("after Update")
print(s1)
print(s2)
'''
#pop
'''
s1 = {1,2,3,4}
s2 = {2,3,4,5}
print("Before Update")
print(s1)
print(s2)
s1.pop()
print("after Update")
print(s1)
print(s2)
'''
#union
'''
s1 = {1,2,3,4}
s2 = {2,3,4,5}
print("Before Update")
print(s1)
print(s2)
print(s1.union(s2))
print("after Update")
print(s1)
print(s2)
'''
#intersection
'''
s1 = {1,2,3,4}
s2 = {2,3,4,5}
print("Before Update")
print(s1)
print(s2)
print(s2.intersection(s1))
print("after Update")
print(s1)
print(s2)
'''
#intersection_update
'''
s1 = {1,2,3,4}
s2 = {2,3,4,5}
print("Before Update")
print(s1)
print(s2)
s2.intersection_update(s1)
print("after Update")
print(s1)
print(s2)
'''
#difference
'''
s1 = {1,2,3,4}
s2 = {2,3,4,5}
print("Before Update")
print(s1)
print(s2)
print(s2.difference(s1))
print("after Update")
print(s1)
print(s2)
'''
#difference_update
'''
s1 = {1,2,3,4}
s2 = {2,3,4,5}
print("Before Update")
print(s1)
print(s2)
s2.difference_update(s1)
print("after Update")
print(s1)
print(s2)
'''
#symmetric_difference
'''
s1 = {1,2,3,4}
s2 = {2,3,4,5}
print("Before Update")
print(s1)
print(s2)
print(s2.symmetric_difference(s1))
print("after Update")
print(s1)
print(s2)
'''
#symmetric_difference_update
'''
s1 = {1,2,3,4}
s2 = {2,3,4,5}
print("Before Update")
print(s1)
print(s2)
s2.symmetric_difference_update(s1)
print("after Update")
print(s1)
print(s2)
'''
#isdisjoint
'''
s1 = {1,2,3}
s2 = {4,5,6}
print("Before Update")
print(s1)
print(s2)
print(s2.isdisjoint(s1))
print("after Update")
print(s1)
print(s2)
'''
#issubset
'''
s1 = {2,3,4}
s2 = {2,3,4,5}
print("Before Update")
print(s1)
print(s2)
print(s1.issubset(s2))
print("after Update")
print(s1)
print(s2)
'''
#issuperset
'''
s1 = {2,3,4}
s2 = {2,3,4,5}
print("Before Update")
print(s1)
print(s2)
print(s2.issuperset(s1))
print("after Update")
print(s1)
print(s2)
'''
#Frozenset
'''
s1 = frozenset([1,2,3,2,3,4])
print(s1)
s1.add(8)
'''













