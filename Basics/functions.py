def average(a, b, c):
    d = (a + b + c) / 3
    # print(d)
    return d
avg = average(1, 2, 3)
print(avg)

def sum(a, b):
    '''
    this is a docstring
    adds two numbers
    '''
    global c
    c = a + b
    return c
c = 12
print(c)
print(sum.__doc__)
print("sum = ",sum(3,5))
# Lamda Functions
square = lambda x : x * x
sum = lambda x, y : x + y

print(square(3))
print(sum(10, 20))

# Recursion~
def fib(n):
    if(n < 2):
        return n
    return fib(n-2) + fib(n-1)
    
print(fib(-3))