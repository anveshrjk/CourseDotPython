import random

cities = ["seoni", "chapara", "lakhnadaun", "dhooma", "bargi", "jabalpur"]

def printLength(list):
    print(len(list))

def printList(list):
    for item in list:
        print(item, end= "\n ")

printLength(cities)
printList(cities)

def fibo(n):
    if(n < 2):
        return 1
    else:
        return fibo(n-2) + fibo(n-1)

print(fibo(5))   

def fact(n):
    if(n < 2):
        return 1
    return n * fact(n-1)
print(fact(5))

def hw(n):
    if(n%2 == 0):
        print("EVEN")
    else:
        print("ODD")
hw(3)
hw(8)

def show(n):
    if(n == 0):
        return
    print(n, end="\n")
    show(n-1)
show(8)

# rock paper scissor
def getChoices():
    playerChoice = input("enter a choice (rock, paper or scissor): ")
    options = ["rock", "paper", "scissor"]
    computerChoice = random.choice(options)
    choices = {"player": playerChoice, "computer": computerChoice}
    if(playerChoice == computerChoice):
        print("draw")
    elif(playerChoice == "paper"):
        if(computerChoice == "scissor"):
            print("computer wins")
        else:
            print("u won")
    elif(playerChoice == "scissor"):
        if(computerChoice == "rock"):
            print("computer won")
        else:
            print("u won")
    elif(playerChoice == "rock"):
        if(computerChoice == "paper"):
            print("computer wins")
        else:
            print("u won")
    return choices
# getChoices()
choices = getChoices()
print(choices)

