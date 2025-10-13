import authenticator, registration_page, profile_page

def main():
    logged_user = ''
    logged_enr = ''
    logged = False
    print("Welcome to LNCT")

    while True:
        # if logged in
        if logged:
            print(f"\nWelcome, {logged_user}!")
            response = input('''
        Choose an option:
        1. Show Profile
        2. Update Profile
        3. Logout
        4. Exit

            Select option 1/2/3/4: ''')

            if response == '1':
                profile_page.show_profile(logged_enr)
            elif response == '2':
                profile_page.update_profile(logged_enr)
            elif response == '3':
                logged, logged_enr, logged_user = authenticator.logout()
                print("You have been logged out.")
            elif response == '4':
                print("Exiting the application. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

        else: # if not logged in
            response = input('''
        Choose an option:
        1. Registration
        2. Login
        3. Exit

            Select option 1/2/3: ''')

            if response == '1':
                registration_page.register()
            elif response == '2':
                logged, logged_enr, logged_user = authenticator.login()
                if not logged:
                    print("Login failed. Please try again.")
            elif response == '3':
                print("Exiting the application. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()