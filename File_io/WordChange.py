with open("practice.txt", "r") as f:
    # f.write("Hello everyone!\nWe are learning File Handling\n")
    # f.write("using Java\nI  like programming in Java")
    data = f.read()
new_data = data.replace("Java", "Python")
print(new_data)

with open("practice.txt", "w") as f:
    f.write(new_data)

import wordCheck  
wordCheck.word_Search()
wordCheck.word_line()
