import authenticator, registration_page, profile_page

logged_user = ''
logged = False

def main():
    print("Welcome in LNCT")
    response = input('''
        Choose option:
        1. Registration
        2. Login
        3. Profile
        4. Update profile
        5. Logout
        6. Main Menu
        7. Exit

            select option 1/2/3/4/5/6/7: ''')

    if response == '1':
        registration_page.register()
    elif response == '2':
        authenticator.login()
    elif response == '3':
        profile_page.show_profile()
    elif response == '4':
        profile_page.update_profile()
    elif response == '5':
        authenticator.logout()
    elif response == '6':
        main()
    elif response == '7':
        authenticator.terminate()
    else:
        print("Invalid Choice, Please select correct option")
        main()
main()
