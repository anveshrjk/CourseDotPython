# def repeat(n):
#     def decorator(func):
#         def wrapper(a):
#             for i in range(n):
#                 func(a)
#         return wrapper
#     return decorator
#
# @repeat(7)
# def say_hello(a):
#     print(f"Hello! {a}")

'''
It replaces the function say_hello with this:
def decorator(func):
    def wrapper(a):
        for i in range(n):
            say_hello(a)
    return wrapper
'''

# say_hello("inte")

import time


def cache(func):
    cache_value = {}
    print(cache_value)

    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]
        result = func(*args)
        cache_value[args] = result
        return result

    return wrapper


@cache
def long_running_function(a, b):
    time.sleep(4)
    return a + b

print(long_running_function(2,3))
print(long_running_function(1,3))
print(long_running_function(4,3))




