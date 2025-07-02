a = int(input("enter day number: \n"))
match a:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")    
    case _:
        print("holiday")

a = input("enter month: \n")
match a:
    case "January" | "March" | "May" | "July" | "August" | "October" | "December":
        print(31)
    case "April" | "June" | "September" | "November":
        print(30)
    case "Feburary":
        print(28)
    case _:
        print("Invalid Input")
                           