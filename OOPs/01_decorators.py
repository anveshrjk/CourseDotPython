'''
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end-start} time")
        return result
    return wrapper

@timer
def example_function(n):
    time.sleep(n)

example_function(5)
'''


def debug(func):
    def wrapper(*args, **kwargs):
        args_value = ', '.join(str(arg) for arg in args)
        kwargs_value = ', '.join(f"{k} = {v}"for k, v in kwargs.items())
        print(f"calling {func.__name__} with args{args_value} and kwargs {kwargs_value}")
        return func(*args, **kwargs)
    return wrapper

@debug
def hello():
    print("helo~")

hello()

@debug
def greet(name, greeting="helo"):
    print(f"{greeting}, {name}")

greet("inte")


# # Decorator is a function that takes a function, it creates a new function inside its body (wrapper). Then it returns that new function
# def decorator(func):
#     def wrapper():
#         print("I am about to execute a function....")
#         func()
#         print("I have executed this function....")
#     return wrapper
#
# @decorator
# def say_hello():
#     print("Hello!")
#
# say_hello()
# # f = decorator(say_hello)
# # f()

'''
f will look something like this
def f():
    print("I am about to execute a function....")
    print("Hello!")
    print("I have executed this function....")
'''

