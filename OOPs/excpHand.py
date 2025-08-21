a = 4
b = 2

try:
    print("resource open")
    print(a/b)
    k = int(input("enter a no: "))
    print(k)

except ZeroDivisionError as e:
    print("ND", e)
except ValueError as e:
    print("invalid input")
finally:
    print("resource closed, bye")