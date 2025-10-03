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

# palindrome
l1 = [1,2,3,2,1]
l2 = [1,2,3]
rev_l1 = l1.copy()
rev_l1.reverse()
if rev_l1 == l1:
    print("palindrome")
else:
    print("not palindrome")