#Compress the string
'''
s = input()
n = len(s)
c = 1
res = ""
for i in range(1,n):
    if s[i] == s[i-1]:
        c = c + 1
    else:
        res = res + s[i-1] + str(c)
        c = 1
res = res + s[-1] + str(c)
print(res)
'''
#Vowels in string
'''
s = input()
for i in s:
    if i not in "aeiouAEIOU":
        print("No")
        break
else:
    print("Yes")
'''
#VC & CC
s = input()
x = "aeiouAEIOU"
vc=cc=0
for i in s:
    if i.isalpha():
        if i in x:
            vc = vc + 1
        else:
            cc = cc + 1
print(vc,cc)



















    
