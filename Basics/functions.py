# def average(a, b, c):
#     d = (a + b + c) / 3
#     # print(d)
#     return d
# avg = average(1, 2, 3)
# print(avg)

# def sum(a, b):
#     '''
#     this is a docstring
#     adds two numbers    
#     '''
#     global c
#     c = a + b
#     return c
# c = 12
# print(c)
# print(sum.__doc__)
# print("sum = ",sum(3,5))
# # Lamda Functions
# square = lambda x : x * x
# sum = lambda x, y : x + y

# print(square(3))
# print(sum(10, 20))

# # Recursion~
# def fib(n):
#     if(n < 2):
#         return n
#     return fib(n-2) + fib(n-1)
    
# print(fib(-3))

#pattern questions
n = int(input("enter pattern length: "))
print("")

# 1 rectangle
def rectangle(n):
    for i in range (0, n):
        for j in range (0, n):
            print("*", end="")
        print("")
rectangle(n)
print("")

# recursive:
def recRectangle(n, row = 0):
    if row == n:
        return
    print('*' * n)
    recRectangle(n, row + 1)
recRectangle(n)
print("")

#2 flag
def flag(n):
    for i in range (0, n):
        for j in range (0, i+1):
            print('*', end="")
        print("")
flag(n)
print("")

# recursive:
def recFlag(n, row = 0):
    if row == n:
        return
    print('*' * (row + 1))
    recFlag(n, row +1)
recFlag(n)
print("")

#increasing number flag
def numFlag(n):
    for i in range (0, n):
        for j in range (0, i+1):
            print(1+j, end="")
        print("")
numFlag(n)
print("")


def numFlag(n):
    for i in range (0, n):
        for j in range (0, i+1):
            print(1+i, end="")
        print("")
numFlag(n)
print("")

# recursive
def recNumFlag(n, row = 0):
    if row == n:
        return
    print(row+1)
    recNumFlag(n, row +1)
recNumFlag(n)
print("")

#print name n times 
def print_name(n):
    if n == 0:
        return
    print("inte")
    print_name(n-1)
print_name(n)

#print 1 to n and n to 1
def oneToN(n):
    num = 0
    if n == 0:
        return
    print(num + 1)
    oneToN(n-1)
oneToN(n)