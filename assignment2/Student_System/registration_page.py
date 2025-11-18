""" Registration Attributes:
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
"""

import csv
import hashlib
import os

STUDENT_DATA_FILE = 'student_data.csv'

def register():
    
    welcome = """---------- Welcome To LNCT Student Portal ----------\n
                Student Registration\n"""
    print(welcome.center(50))

    # attributes
    headers = [
        'Enrollment No', 'Password Hash', 'Full Name', 'Class Roll No', 
        'Batch', 'Branch', 'Semester', 'Section', 'Ph No', 
        "Father's Name", "Mother's Name", "Parent's Ph No", 'Permanent Address'
    ]

    # is the data already exists?
    if not os.path.exists(STUDENT_DATA_FILE):
        with open(STUDENT_DATA_FILE, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(headers)

    # enrollment no.
    while True:
        enrollment_no = input("Enter Enrollment Number: ").strip().upper()
        if len(enrollment_no) != 12:
            print("Invalid Enrollment Number. It must be 12 characters long.")
            continue
        
        # if enrollment no already exists
        is_unique = True
        with open(STUDENT_DATA_FILE, 'r', newline='') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if row[0] == enrollment_no:
                    is_unique = False
                    break
        
        if is_unique:
            break
        else:
            print("This Enrollment Number is already registered. Please login.")
            return

    # password
    while True:
        password = input("Set Password (min 6 chars, letters & numbers only): ").strip()
        if len(password) >= 6 and password.isalnum():
            # Hash the password for secure storage
            password_hash = hashlib.sha256(password.encode()).hexdigest()
            break
        else:
            print("Invalid password format. Please follow the rules.")

    # full name
    while True:
        full_name = input("Enter your Full Name: ").strip().title()
        # Replace spaces to check if the rest is alphabetic
        if len(full_name) > 2 and all(char.isalpha() or char.isspace() for char in full_name):
            break
        else:
            print("Please enter a valid name (letters and spaces only).")
            
    # class roll no
    while True:
        class_roll_no = input("Enter your Class Roll No.: ").strip()
        if class_roll_no.isdigit():
            break
        else:
            print("Please enter a valid roll number (digits only).")

    # batch
    while True:
        batch = input("Enter Batch (e.g., BTech, BPharma): ").strip().upper()
        if batch in ["BTECH", "BPHARMA", "MCA", "MBA"]: # Add more batches if needed
            break
        else:
            print("Invalid Batch. Please enter a valid one.")

    # branch
    while True:
        branch = input("Enter Branch (e.g., CSE, ME, EC): ").strip().upper()
        if len(branch) > 1 and branch.isalpha():
            break
        else:
            print("Please enter a valid branch name.")
            
    # semester
    while True:
        semester = input("Enter Semester (1-8): ").strip()
        if semester.isdigit() and 1 <= int(semester) <= 8:
            break
        else:
            print("Please enter a valid semester (a number from 1 to 8).")

    # section
    while True:
        section = input("Enter Section (e.g., A, B, A1): ").strip().upper()
        if len(section) > 0:
            break
        else:
            print("Section cannot be empty.")

    # phone number
    while True:
        ph_no = input("Enter your 10-digit Phone Number: ").strip()
        if ph_no.isdigit() and len(ph_no) == 10:
            break
        else:
            print("Please enter a valid 10-digit phone number.")

    # father's name
    while True:
        fathers_name = input("Enter Father's Name: ").strip().title()
        if len(fathers_name) > 2 and all(char.isalpha() or char.isspace() for char in fathers_name):
            break
        else:
            print("Please enter a valid name (letters and spaces only).")

    # mother's name
    while True:
        mothers_name = input("Enter Mother's Name: ").strip().title()
        if len(mothers_name) > 2 and all(char.isalpha() or char.isspace() for char in mothers_name):
            break
        else:
            print("Please enter a valid name (letters and spaces only).")
            
    # parent's phone number
    while True:
        parents_ph_no = input("Enter Parent's 10-digit Phone Number: ").strip()
        if parents_ph_no.isdigit() and len(parents_ph_no) == 10:
            break
        else:
            print("Please enter a valid 10-digit phone number.")
            
    #  permanent address
    while True:
        address = input("Enter Permanent Address: ").strip()
        if len(address) > 10:
            break
        else:
            print("Address seems too short. Please enter a full address.")

    # save all data to the CSV file
    student_record = [
        enrollment_no, password_hash, full_name, class_roll_no, 
        batch, branch, semester, section, ph_no, 
        fathers_name, mothers_name, parents_ph_no, address
    ]

    with open(STUDENT_DATA_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(student_record)

    print("\nRegistration Successful! You can now log in.")

register()

# if __name__ == "__main__":
#     register()
