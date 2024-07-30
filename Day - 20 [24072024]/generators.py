'''
def hello():
    for i in range(1,6):
        yield i
x = hello()
for i in x:
    print(i)
'''
'''
def infinite_even():
    n = 0
    while True:
        yield n
        n = n + 2
z = infinite_even()
for i in range(100):
    print(next(z))
'''

        
