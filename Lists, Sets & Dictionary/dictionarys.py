# dictionaries are key value pairs and facilitates faster look-ups~
enr = {"inte": 39, "rose": 38}
print(enr, type(enr))

# list is not hashable, else are~

print(enr["inte"])

#methods
print(enr.keys())
print(enr.values())

# marks.pop("rose")
# print(marks)

# marks.clear()
# print(marks)

print(enr.items())

print(enr.get("inte"))

new_dict = {"nooby" : 3}
enr.update(new_dict)
print(enr)

#comprehension
table_of_5 = {i: 5 * i for i in range(1, 11)}
print(table_of_5)

