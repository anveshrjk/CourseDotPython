class Student():
    enroll_no: str
    name: str
    password: str
    age: int
    email: str

    def __str__(self):
        return f"Name: {self.name}, Enroll No: {self.enroll_no}, Age: {self.age}, Email: {self.email}"


# --- Global Variables ---
logged = False
current_user = None
users = []
no_of_users = 1

# Creating a default admin user for testing
'''
admin = Student()
admin.name = "admin"
admin.password = "admin123"
users.append(admin)
'''


def is_user_existing(user_name):
    global users
    for user in users:
        if user.name == user_name:
            return True
    return False


def register():
    temp = Student()
    user_name = ""
    pswd_final = ""
    global no_of_users
    global users

    user_name = input("Enter you username: ")
    while True:
        if is_user_existing(user_name):
            print("The username already exists. Try another username.")
            user_name = input("Enter you username: ")
        else:
            break

    while True:
        pswd_initial = input("Enter your password: ")
        pswd_confirm = input("Enter your password again for confirmation: ")
        if pswd_initial == pswd_confirm:
            pswd_final = pswd_confirm
            break
        else:
            print("Passwords do not match. Please try again.")

    try:
        temp.age = int(input("Enter your age: "))
    except ValueError:
        print("Wrong input! Age not set. You can update it later.")
        temp.age = 0  # Default age

    email = input("Enter your email: ")
    enroll_no = "0176_" + str(no_of_users + 1)

    temp.name = user_name
    temp.password = pswd_final
    temp.email = email
    temp.enroll_no = enroll_no

    users.append(temp)
    no_of_users += 1
    print("\n✅ Registration successful!")
    print("Your details:", temp)


def login():
    global logged, current_user, users

    if logged:
        print("You are already logged in.")
        return

    user_name = input("Enter your username: ")
    password = input("Enter your password: ")

    for user in users:
        if user.name == user_name and user.password == password:
            logged = True
            current_user = user
            print(f"\nWelcome, {user.name}! You are now logged in.")
            return
    # if the loop finishes without finding a match
    print("\nInvalid username or password.")


def show_profile():
    global logged
    global current_user

    if logged:
        print("\n--- Your Profile ---")
        print(current_user)
    else:
        print("\nYou need to be logged in to view your profile.")


def update_profile():
    global logged
    global current_user

    if not logged:
        print("\nYou need to be logged in to update your profile.")
        return

    print("\n--- Update Profile ---")
    print("What would you like to update?")
    choice = input("1. Password\n2. Age\n3. Email\nEnter your choice: ")

    if choice == '1':
        new_pass = input("Enter new password: ")
        current_user.password = new_pass
        print("Password updated successfully!")
    elif choice == '2':
        try:
            new_age = int(input("Enter new age: "))
            current_user.age = new_age
            print("Age updated successfully!")
        except ValueError:
            print("Invalid input. Please enter a number for age.")
    elif choice == '3':
        new_email = input("Enter new email: ")
        current_user.email = new_email
        print("Email updated successfully!")
    else:
        print("Invalid choice.")


def logout():
    global logged
    global current_user

    if logged:
        logged = False
        current_user = None
        print("\nYou have been successfully logged out.")
    else:
        print("\nYou are not logged in.")


def terminate():
    print("\nThank you for using the system. Goodbye!")
    exit()


def main():
    print("\nWelcome to the Student Portal")
    while True:
        response = input('''
        --- Main Menu ---
        1. Register
        2. Login
        3. Show Profile
        4. Update Profile
        5. Logout
        6. Exit
        -------------------
        Select an option: ''')

        if response == '1':
            register()
        elif response == '2':
            login()
        elif response == '3':
            show_profile()
        elif response == '4':
            update_profile()
        elif response == '5':
            logout()
        elif response == '6':
            terminate()
        else:
            print("\nInvalid Choice. Please select a correct option.")


if __name__ == "__main__":
    main()