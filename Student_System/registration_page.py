''' Registration Attributes:
        Enrollment No. 0176cs231039
        Password
        Full name
        Class Roll No.
        Batch
        Branch
        Semester
        Section
        Ph No.
        Father's Name
        Mother's Name
        Parent's Ph No.
        Permanent Address
'''

def register():
    
    welcome = """---------- Welcome To LNCT Student Portal ----------\n
                Student Registration\n"""
    print(welcome.center(50))

    # Enrollment no.
    while True:
        enrollment_no = input("Enrollment Number:\n")
        enrollment_no = enrollment_no.upper()

        if len(enrollment_no) == 12:
            break
        else:
            print("Invalid Enrollment Number")

    # Password
    while True:
        password = input("Set Password:\n")
        if len(password) >= 6:
            if password.isalnum() == True:
                break
            else:
                print("Password must be Alpha-numeric")
        else:
            print("Minimum Password length: 6")

    # Student's name
    while True:
        full_name = input("Student's Name:\n")
        if full_name.isalnum() == False:
            break
        else:
            print("Enter a valid name")

    # Batch
    while True:
        batch = input("Batch (BTech/BPharma):\n")
        batch = batch.upper()
        if batch == "BTECH" or batch == "BPHARMA":
            break
        else:
            print("Invalid Batch")
register()
