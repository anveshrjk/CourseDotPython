import csv
import os

STUDENT_DATA_FILE = 'student_data.csv'


def show_profile(enrollment_no):
    print("\n--- Your Profile ---")
    try:
        with open(STUDENT_DATA_FILE, 'r', newline='') as file:
            reader = csv.reader(file)
            headers = next(reader)

            for row in reader:
                if row[0] == enrollment_no:
                    for header, value in zip(headers, row):
                        if header != 'Password Hash':
                            print(f"{header}: {value}")
                    return
    except FileNotFoundError:
        print("Error: Student data file not found.")


def update_profile(enrollment_no):
    print("\n--- Update Your Profile ---")

    try:
        with open(STUDENT_DATA_FILE, 'r', newline='') as file:
            reader = csv.reader(file)
            all_records = list(reader)
            headers = all_records[0]
    except FileNotFoundError:
        print("Error: Student data file not found.")
        return

    user_record = None
    record_index = -1
    for i, record in enumerate(all_records):
        if record[0] == enrollment_no:
            user_record = record
            record_index = i
            break

    if not user_record:
        print("Error: Could not find your profile.")
        return

    fields_to_update = {
        '1': 'Ph No',
        '2': 'Parent\'s Ph No',
        '3': 'Permanent Address'
    }

    print("Which field would you like to update?")
    for key, value in fields_to_update.items():
        print(f"{key}. {value}")

    choice = input("Select an option (1-3): ").strip()

    if choice in fields_to_update:
        field_name = fields_to_update[choice]
        field_index = headers.index(field_name)

        new_value = input(f"Enter new value for {field_name}: ").strip()

        all_records[record_index][field_index] = new_value

        temp_file = 'student_data_temp.csv'
        with open(temp_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(all_records)

        os.remove(STUDENT_DATA_FILE)
        os.rename(temp_file, STUDENT_DATA_FILE)

        print("\nProfile updated successfully!")
    else:
        print("Invalid choice. No changes were made.")