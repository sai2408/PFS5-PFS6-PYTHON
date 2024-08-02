#Access specifiers
#Public Access Specifier
'''
class xyz:
    value = 0
    def __init__(self):
        self.value = 100
    def display(self):
        print(self.value)
obj = xyz()
obj.display()
obj.value = 200
obj.display()
'''
#Private Access Specifier
'''
class xyz:
    __value = 0
    def __init__(self):
        self.__value = 100
    def display(self):
        print(self.__value)
obj = xyz()
obj.display()
obj.__value = 200
obj.display()
'''
#Encapsulation
'''
class car:
    def fuel(self):
        print("Fuel : 75%")
    def indicator(self):
        print("Left indicatior Enabled")
    def speedometer(self):
        print("Speed 100km/hr")
    def __init__(self):
        print("I am Odometer")
        self.fuel()
        self.indicator()
        self.speedometer()
c1 = car()
'''

        















