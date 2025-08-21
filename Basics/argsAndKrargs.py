from functools import reduce

# args:

# def sum(*args):
#     print(args)
#     total = 0
#     for item in args:
#         total += item
#     return total

# print(sum(30,7,1))

def sum(*args):
    print(args)
    return reduce(lambda x, y: x + y, args, 0)

print(sum(30,7,1))

# kwargs
def marks(**kwargs):
    for item in kwargs.keys():
        print(f"the marks of {item} is {kwargs[item]}")

marks(inte = 39, rose = 38, nooby = 3)