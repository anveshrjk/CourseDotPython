import csv
import hashlib

STUDENT_DATA_FILE = 'student_data.csv'


def login():
    print("\n--- Student Login ---")
    enrollment_no = input("Enter Enrollment Number: ").strip().upper()
    password = input("Enter Password: ").strip()

    try:
        # taken password is
        password_hash = hashlib.sha256(password.encode()).hexdigest()

        with open(STUDENT_DATA_FILE, 'r', newline='') as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                if row[0] == enrollment_no and row[1] == password_hash:
                    print(f"\nLogin Successful. Welcome, {row[2]}!")
                    return True, row[0], row[2]

            return False, ''

    except FileNotFoundError:
        print("No student data found. Please register first.")
        return False, ''


def logout():
    return False, ''


def terminate():
    print("\nApplication closed.")
    exit()