marks = [32, 43, 54, 63, 53]
extra_marks = [20, 60]
mixed = [16, "helo", True, 125.6]

marks.append(39)  #it'll add the respective element in the end of list.
print(marks)
print(mixed)

print(marks[1:3])
print(mixed[3]) 

marks.extend(extra_marks)
print(marks)
mixed.pop()