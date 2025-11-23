import os
import json
import random
from datetime import datetime
from getpass import getpass

# filenames for persistence
USERS_FILE = "users.json"
QUESTIONS_FILE = "questions.json"
SCORES_FILE = "scores.json"

class Student:
    def __init__(self, enroll_no="", name="", password="", age=0, email="", role="user", contact=""):
        self.enroll_no = enroll_no
        self.name = name
        self.password = password
        self.age = age
        self.email = email
        self.role = role
        self.contact = contact

    def to_dict(self):
        return {
            "enroll_no": self.enroll_no,
            "name": self.name,
            "password": self.password,
            "age": self.age,
            "email": self.email,
            "role": self.role,
            "contact": self.contact
        }

    @staticmethod
    def from_dict(d):
        return Student(
            enroll_no=d.get("enroll_no",""),
            name=d.get("name",""),
            password=d.get("password",""),
            age=d.get("age",0),
            email=d.get("email",""),
            role=d.get("role","user"),
            contact=d.get("contact","")
        )

    def __str__(self):
        return f"Name: {self.name}, Enroll No: {self.enroll_no}, Age: {self.age}, Email: {self.email}, Contact: {self.contact}, Role: {self.role}"

# ---------------- storage helpers ----------------
def load_json(path, default):
    if not os.path.exists(path):
        return default
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return default

def save_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def ensure_files_exist():
    users = load_json(USERS_FILE, {})
    if not users:
        admin = Student(enroll_no="0000_ADMIN", name="admin", password="admin123", age=0, email="admin@local", role="admin")
        users = {"admin": admin.to_dict()}
        save_json(USERS_FILE, users)

    questions = load_json(QUESTIONS_FILE, {})
    if not questions:
        q = {
            "DSA": [
                {"q":"What is the time complexity of binary search?","opts":["A. O(n)","B. O(log n)","C. O(n log n)","D. O(1)"],"ans":"B"},
                {"q":"Which data structure uses FIFO?","opts":["A. Stack","B. Tree","C. Queue","D. Graph"],"ans":"C"},
                {"q":"What is the worst-case for quicksort?","opts":["A. O(n log n)","B. O(n^2)","C. O(n)","D. O(log n)"],"ans":"B"},
                {"q":"Which DS is best for LRU cache?","opts":["A. Array","B. Hash + Doubly Linked List","C. Stack","D. Tree"],"ans":"B"},
                {"q":"Which structure gives average O(1) lookup?","opts":["A. List","B. Hash Table","C. Tree","D. Heap"],"ans":"B"}
            ],
            "DBMS": [
                {"q":"What does SQL stand for?","opts":["A. Simple Query Language","B. Structured Query Language","C. Standard Query Language","D. None"],"ans":"B"},
                {"q":"Which property ensures all-or-nothing in transactions?","opts":["A. Atomicity","B. Consistency","C. Isolation","D. Durability"],"ans":"A"},
                {"q":"Primary key must be:","opts":["A. Nullable","B. Unique","C. Non-unique","D. Duplicate allowed"],"ans":"B"},
                {"q":"Normalization avoids:","opts":["A. Redundancy","B. Speed","C. Backups","D. Indexing"],"ans":"A"},
                {"q":"JOIN that returns rows present in both tables is called:","opts":["A. LEFT JOIN","B. RIGHT JOIN","C. INNER JOIN","D. FULL JOIN"],"ans":"C"}
            ],
            "PYTHON": [
                {"q":"What type is returned by input() in Python3?","opts":["A. int","B. float","C. str","D. bool"],"ans":"C"},
                {"q":"How do you create a list comprehension?","opts":["A. {x for x in y}","B. [x for x in y]","C. (x for x in y)","D. <x for x in y>"],"ans":"B"},
                {"q":"Which keyword defines a function in Python?","opts":["A. func","B. def","C. function","D. lambda"],"ans":"B"},
                {"q":"Mutable built-in type is:","opts":["A. tuple","B. str","C. list","D. frozenset"],"ans":"C"},
                {"q":"To handle exceptions we use:","opts":["A. if","B. for","C. try/except","D. switch"],"ans":"C"}
            ]
        }
        save_json(QUESTIONS_FILE, q)

    scores = load_json(SCORES_FILE, [])
    if not isinstance(scores, list):
        save_json(SCORES_FILE, [])

# ---------------- user management ----------------
def get_all_users():
    raw = load_json(USERS_FILE, {})
    return {k: Student.from_dict(v) for k, v in raw.items()}

def save_all_users(user_map):
    raw = {k: v.to_dict() for k, v in user_map.items()}
    save_json(USERS_FILE, raw)

def is_user_existing(user_map, user_name):
    return user_name in user_map

# ---------------- globals ----------------
current_user = None

def register():
    users = get_all_users()
    username = input("Enter your username: ").strip()
    while not username or is_user_existing(users, username):
        print("Invalid or already existing username. Try again.")
        username = input("Enter your username: ").strip()

    while True:
        pwd = getpass("Enter your password: ").strip()
        pwd2 = getpass("Confirm password: ").strip()
        if pwd == pwd2 and pwd:
            break
        print("Passwords do not match or empty. Try again.")

    try:
        age = int(input("Enter your age: ").strip())
    except Exception:
        age = 0

    email = input("Enter your email: ").strip()
    contact = input("Enter contact number (optional): ").strip()
    enroll_no = f"0176_{len(users)+1:03d}"

    s = Student(enroll_no=enroll_no, name=username, password=pwd, age=age, email=email, role="user", contact=contact)
    users[username] = s
    save_all_users(users)
    print("\n✅ Registration successful!")
    print("Your details:", s)

def login():
    global current_user
    if current_user:
        print("Already logged in.")
        return
    users = get_all_users()
    username = input("Enter your username: ").strip()
    pwd = getpass("Enter your password: ").strip()
    user = users.get(username)
    if user and user.password == pwd:
        current_user = user
        print(f"\nWelcome, {user.name}! (role: {user.role})")
    else:
        print("\nInvalid username or password.")

def logout():
    global current_user
    if current_user:
        print(f"\n{current_user.name} logged out.")
        current_user = None
    else:
        print("\nNot logged in.")

def show_profile():
    if not current_user:
        print("\nYou need to login to view profile.")
        return
    print("\n--- Your Profile ---")
    print(current_user)

def update_profile():
    if not current_user:
        print("\nYou need to login to update profile.")
        return
    print("\nLeave blank to keep current.")
    new_name = input(f"Name [{current_user.name}]: ").strip()
    if new_name:
        current_user.name = new_name
    new_pwd = getpass("New password (leave blank to keep): ").strip()
    if new_pwd:
        current_user.password = new_pwd
    try:
        new_age = input(f"Age [{current_user.age}]: ").strip()
        if new_age:
            current_user.age = int(new_age)
    except Exception:
        print("Invalid age input; keeping old.")
    new_email = input(f"Email [{current_user.email}]: ").strip()
    if new_email:
        current_user.email = new_email
    new_contact = input(f"Contact [{current_user.contact}]: ").strip()
    if new_contact:
        current_user.contact = new_contact

    users = get_all_users()
    users[current_user.name] = current_user
    # if username changed we need to fix key (simple approach: rebuild map)
    # rebuild map to ensure unique keys
    rebuilt = {}
    for u in users.values():
        rebuilt[u.name] = u
    save_all_users(rebuilt)
    print("Profile updated.")

# ---------------- quiz ----------------
def attempt_quiz():
    if not current_user:
        print("\nLogin required.")
        return
    questions = load_json(QUESTIONS_FILE, {})
    cats = list(questions.keys())
    if not cats:
        print("No categories available.")
        return
    print("\nCategories:")
    for i, c in enumerate(cats, 1):
        print(f"{i}. {c}")
    choice = input("Select category number: ").strip()
    if not choice.isdigit() or int(choice)-1 not in range(len(cats)):
        print("Invalid selection.")
        return
    cat = cats[int(choice)-1]
    qlist = questions.get(cat, [])
    if not qlist:
        print("No questions in this category.")
        return

    # choose between 5 and 10 questions depending on availability
    n = min(10, max(5, len(qlist))) if len(qlist) >=5 else len(qlist)
    selected = random.sample(qlist, k=n)
    random.shuffle(selected)
    score = 0
    for idx, q in enumerate(selected, 1):
        print(f"\nQ {idx}/{len(selected)}: {q['q']}")
        for opt in q['opts']:
            print(" ", opt)
        ans = input("Your answer (A/B/C/D): ").strip().upper()
        if ans == q.get("ans","").upper():
            score += 1
    print(f"\nResult: {score} / {len(selected)}")

    scores = load_json(SCORES_FILE, [])
    entry = {
        "user": current_user.name,
        "enroll": current_user.enroll_no,
        "category": cat,
        "score": score,
        "total": len(selected),
        "datetime": datetime.now().isoformat()
    }
    scores.append(entry)
    save_json(SCORES_FILE, scores)
    print("Score saved.")

def show_my_scores():
    if not current_user:
        print("\nLogin required.")
        return
    scores = load_json(SCORES_FILE, [])
    mine = [s for s in scores if s.get("user") == current_user.name]
    if not mine:
        print("No attempts yet.")
        return
    print("\nYour Attempts:")
    for s in mine:
        print(f"{s['datetime']} | {s['category']} | {s['score']}/{s['total']}")

# ---------------- admin ----------------
def admin_menu():
    if not current_user or current_user.role != "admin":
        print("Admin access only.")
        return
    while True:
        print("""
Admin Menu:
1. Add Question
2. View All Scores
3. Back
""")
        c = input("Choice: ").strip()
        if c == "1":
            add_question()
        elif c == "2":
            view_all_scores()
        elif c == "3":
            break
        else:
            print("Invalid choice.")

def add_question():
    qdata = load_json(QUESTIONS_FILE, {})
    cat = input("Category (existing or new): ").strip()
    qtext = input("Question text: ").strip()
    opts = []
    for label in ("A","B","C","D"):
        opts.append(f"{label}. {input(f'Option {label}: ').strip()}")
    ans = input("Correct option (A/B/C/D): ").strip().upper()
    item = {"q": qtext, "opts": opts, "ans": ans}
    qdata.setdefault(cat, []).append(item)
    save_json(QUESTIONS_FILE, qdata)
    print("Question added.")

def view_all_scores():
    scores = load_json(SCORES_FILE, [])
    if not scores:
        print("No scores recorded.")
        return
    for s in scores:
        print(f"{s.get('datetime')} | {s.get('user')} | {s.get('category')} | {s.get('score')}/{s.get('total')}")

# ---------------- main menu ----------------
def main_menu():
    ensure_files_exist()
    while True:
        print("""
--- Main Menu ---
1. Register
2. Login
3. Show Profile
4. Update Profile
5. Attempt Quiz
6. Show My Scores
7. Admin Panel
8. Logout
9. Exit
------------------
""")
        choice = input("Select option: ").strip()
        if choice == '1':
            register()
        elif choice == '2':
            login()
        elif choice == '3':
            show_profile()
        elif choice == '4':
            update_profile()
        elif choice == '5':
            attempt_quiz()
        elif choice == '6':
            show_my_scores()
        elif choice == '7':
            admin_menu()
        elif choice == '8':
            logout()
        elif choice == '9':
            print("Goodbye.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main_menu()