# map(), reduce() & filter()
from functools import reduce

numbers = [1, 2, 3]

#map
result = map(lambda a : a * 2, numbers)
print(list(result))

#filter...pta nhi yr

#reduce
expences = [('Dinner', 80), ('Car repair', 120)]

sum  = reduce(lambda a, b : a[1] + b[1], expences)
print(sum)
print(reduce(12,3))