# Create a list containing table of 5

# normal method
# a = 5
# table = []

# for i in range(1, 11):
#     table.append(5 * i)

# list comprehension method
table = [5 * i for i in range(1, 11)]
print(table)