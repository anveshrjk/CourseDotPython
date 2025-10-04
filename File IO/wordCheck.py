word = input("enter the word to search:\n")

def word_Search():
    
    with open("practice.txt", "r") as f:
        data = f.read()
        if word in data:
            print("found")
        else:
            print("not found")

def word_line():
    data = True
    line_no = 1
    with open("practice.txt", "r") as f:
        while data:
            data = f.readline()
            if word in data:
                print(line_no)
                return
            line_no += 1
    return -1