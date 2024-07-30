#Built in
'''
import random
x = random.randint(5,10)
print(x)
'''
#User defined
'''
import sample1
import module2
print(sample1.a)
sample1.hello()
module2.hello()
print(module2.x)
'''
#Files
#Read
'''
f = open("abc.txt","r")
print(f.read())
f.close()
'''
#Write
'''
f = open("xyz.txt","w")
f.write("Another New File Created")
f.close()
'''
#Append
'''
f = open("abc.txt","a")
f.write("New string inserted")
f.close()
'''
'''
f = open("mno.txt","a")
f.write("New file 1")
f.close()
'''
#Read and write
f = open("abc.txt","a+")
f.write("Codegnan IT Solutions")
f.seek(0)
print(f.read())
f.close()

















