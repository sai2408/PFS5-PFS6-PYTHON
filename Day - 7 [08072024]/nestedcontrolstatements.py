#Pattern - 1
'''
# # #
# # #
# # #
'''
'''
for i in range(3):
    for j in range(3):
        print("#",end=" ")
    print()
'''
#Pattern - 2
'''
#
# #
# # #
# # # #
# # # # #
'''
'''
for i in range(5):
    for j in range(5):
        if j <= i:
            print("#",end=" ")
    print()
'''
#Pattern - 3
'''
1 1 1 1 1
2 2 2 2 2
3 3 3 3 3
4 4 4 4 4
5 5 5 5 5
'''
#Approach - 1
'''
x = 1
for i in range(5):
    for j in range(5):
        print(x,end=" ")
    x = x + 1
    print()
'''
#Approach - 2
'''
for i in range(5):
    for j in range(5):
        print(i+1,end=" ")
    print()
'''
#approach - 3
'''
for i in range(1,6):
    x = str(i)+" "
    print(x*5)
'''
#Pattern - 4
'''
1 2 3
4 5 6
7 8 9
'''
'''
x = 1
for i in range(3):
    for j in range(3):
        print(x,end=" ")
        x = x + 1
    print()
'''
#Pattern - 5
'''
n -> 5
# # # # #
# # # #
# # #
# #
#
'''
'''
for i in range(5):
    for j in range(5):
        if (i<=j):
            print("#",end=" ")
    print()
'''
#Pattern - 6
'''
n -> 5
#
# #
# # #
# # # #
# # # # #
# # # #
# # #
# #
#
'''
'''
for i in range(5):
    for j in range(5):
        if j <= i:
            print("#",end=" ")
    print()
for i in range(4):
    for j in range(4):
        if (i<=j):
            print("#",end=" ")
    print()
'''
#Pattern - 7
'''
n -> 5
# # # # # -> 0
1 2 3 4 5 -> 1
# # # # # -> 2
1 2 3 4 5 -> 3
# # # # # -> 4
'''
'''
x = 1
for i in range(5):
    for j in range(5):
        if i%2 == 0:
            print("#",end=" ")
        else:
            print(x,end=" ")
            x = x + 1
    x = 1
    print()
'''         
#Pattern - 8
'''
# # # # #
# @ @ @ #
# @ @ @ #
# @ @ @ #
# # # # #
'''
'''
n = int(input())
for i in range(n):
    for j in range(n):
        if (i==0 or j==0 or i==n-1 or j==n-1):
            print("#",end=" ")
        else:
            print("@",end=" ")
    print()
'''
#Pattern - 9
'''
# # # # #
#       #
#       #
#       #
# # # # #
'''
'''
n = int(input())
for i in range(n):
    for j in range(n):
        if (i==0 or j==0 or i==n-1 or j==n-1):
            print("#",end=" ")
        else:
            print(" ",end=" ")
    print()
'''
#Pattern - 10
'''
1
1 2
1   3
1     4
1 2 3 4 5
'''
#Pattern - 11
'''
        5
      4 5
    3   5
  2     5
1 2 3 4 5
'''
























































    





















            









