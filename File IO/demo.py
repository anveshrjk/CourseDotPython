try:
    f = open("DS_use.txt", "r")

    content = f.read()
    print(content)
    f.close()
except FileNotFoundError as e:
    print("File Not Found")

    
i = open("inte.txt", "w")

string = '''
inte is a pen name of mine.
it individually doesn't mean anything,
but it sounds cool.
i use it for games and stuffs.
'''

i.write(string)
i.close()