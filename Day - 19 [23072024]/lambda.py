#function
'''
def add(a,b):
    return (a+b)
print(add(10,20))

add = lambda a,b : a+b
print(add(10,20))
'''
#Lambda with Filter
'''
x = [10,11,12,13,14,15]
res = list(filter(lambda a : a%2==0,x))
print(res)
'''
#lambda with Map
'''
x = [99,199,299,399]
res = list(map(lambda a : a+1,x))
print(res)
'''
