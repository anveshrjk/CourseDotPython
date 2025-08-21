# dictionaries are key value pairs and facilitates faster look-ups~
marks = {"inte": 39, "rose": 38}
print(marks, type(marks))

# list is not hashable, else are~

print(marks["inte"])

#methods
print(marks.keys())
print(marks.values())

marks.pop("rose")
print(marks)

marks.clear()
print(marks)

#comprehension
table_of_5 = {i: 5 * i for i in range(1, 11)}
print(table_of_5)