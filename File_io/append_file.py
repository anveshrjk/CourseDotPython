# append to an existing file named inte.txt
# it should add details about inte name origin  (LoL?)

i = open("inte.txt", "a")

string = '''
inte was originally "integration"
but later i minimized it to inte...
so that it wouldn't feel like a nerd~
'''

i.write(string)
i.close()