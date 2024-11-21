import os
import json
import getpass

USER_DATA_FILE = "user_data.json"
QUIZ_RESULTS_FILE = "quiz_results.json"

questions = {
    "Python": {
        "What is the output of print(2 ** 3)?": {"a": "6", "b": "9", "c": "8", "d": "5", "answer": "c"},
        "Which data type is immutable in Python?": {"a": "List", "b": "Dictionary", "c": "Set", "d": "Tuple", "answer": "d"},
        "What keyword is used to define a function in Python?": {"a": "func", "b": "def", "c": "function", "d": "create", "answer": "b"},
        "What is the correct file extension for Python files?": {"a": ".pt", "b": ".py", "c": ".pyt", "d": ".python", "answer": "b"},
        "What will len([1, 2, 3, 4]) return?": {"a": "4", "b": "3", "c": "5", "d": "Error", "answer": "a"},
        "What is the result of print('Hello' + 'World')?": {"a": "Hello World", "b": "HelloWorld", "c": "Hello+World", "d": "Error", "answer": "b"},
        "Which operator is used for floor division?": {"a": "/", "b": "//", "c": "%", "d": "**", "answer": "b"},
        "What will print(10 // 3) output?": {"a": "3.333", "b": "3", "c": "4", "d": "Error", "answer": "b"},
        "What does the continue statement do in Python?": {"a": "Ends the loop", "b": "Skips the rest of the code inside the loop", "c": "Exits the program", "d": "Repeats the current iteration", "answer": "b"},
        "What is the correct way to create an empty dictionary in Python?": {"a": "{}", "b": "[]", "c": "()", "d": "dict()", "answer": "d"},
        "What is the output of print(type(5))?": {"a": "<type 'int'>", "b": "<class 'int'>", "c": "<type 'integer'>", "d": "<class 'integer'>", "answer": "b"},
        "Which function is used to convert a string to lowercase?": {"a": "toLowerCase()", "b": "lower()", "c": "toLower()", "d": "lowercase()", "answer": "b"},
        "What is the correct syntax to create a class in Python?": {"a": "class MyClass {}", "b": "class MyClass():", "c": "def MyClass()", "d": "create MyClass()", "answer": "b"},
        "What is the output of print(type([]))?": {"a": "<type 'list'>", "b": "<class 'list'>", "c": "<type 'array'>", "d": "<class 'array'>", "answer": "b"},
        "What is the result of 5 > 3 and 2 < 1?": {"a": "True", "b": "False", "c": "Error", "d": "None", "answer": "b"},
    },
    "DBMS": {
        "What does SQL stand for?": {"a": "Structured Query Language", "b": "Sequence Query Language", "c": "Structured Question Language", "d": "Sequential Question Language", "answer": "a"},
        "Which of these is a type of join in SQL?": {"a": "Outer", "b": "Inner", "c": "Full", "d": "All of the above", "answer": "d"},
        "What does ACID stand for in databases?": {"a": "Atomicity, Consistency, Isolation, Durability", "b": "Accuracy, Consistency, Isolation, Durability", "c": "Atomicity, Completeness, Isolation, Durability", "d": "Atomicity, Consistency, Integrity, Durability", "answer": "a"},
        "What is a primary key?": {"a": "A unique identifier for a table record", "b": "A key that allows duplicate values", "c": "A key that references another table", "d": "None of the above", "answer": "a"},
        "What does the GROUP BY clause do in SQL?": {"a": "Sorts the data", "b": "Groups rows that have the same values", "c": "Deletes duplicate rows", "d": "Joins multiple tables", "answer": "b"},
        "Which SQL clause is used to filter rows?": {"a": "WHERE", "b": "SELECT", "c": "ORDER BY", "d": "GROUP BY", "answer": "a"},
        "What is a foreign key?": {"a": "A key that uniquely identifies a row in a table", "b": "A key that references the primary key in another table", "c": "A key used to sort records", "d": "None of the above", "answer": "b"},
        "Which of these is a NoSQL database?": {"a": "MySQL", "b": "MongoDB", "c": "PostgreSQL", "d": "Oracle", "answer": "b"},
        "What is normalization in databases?": {"a": "Increasing database size", "b": "Reducing redundancy and dependency", "c": "Creating duplicate tables", "d": "None of the above", "answer": "b"},
        "What is the default isolation level in most databases?": {"a": "Read Uncommitted", "b": "Read Committed", "c": "Repeatable Read", "d": "Serializable", "answer": "b"},
        "What is a transaction in DBMS?": {"a": "A set of operations performed as a single logical unit", "b": "A single SQL query", "c": "A record in a table", "d": "None of the above", "answer": "a"},
        "Which command is used to modify existing data in a database?": {"a": "SELECT", "b": "DELETE", "c": "UPDATE", "d": "INSERT", "answer": "c"},
        "What is a view in SQL?": {"a": "A temporary table", "b": "A virtual table based on a SQL query", "c": "A copy of a table", "d": "None of the above", "answer": "b"},
        "What is the purpose of the HAVING clause?": {"a": "Filter rows in a SELECT statement", "b": "Filter groups in a GROUP BY statement", "c": "Sort rows", "d": "None of the above", "answer": "b"},
        "What is a database index?": {"a": "A tool to speed up data retrieval", "b": "A duplicate copy of a table", "c": "A backup of the database", "d": "None of the above", "answer": "a"},
    },
    "DSA": {
       "Which data structure uses LIFO order?": {"a": "Queue", "b": "Stack", "c": "Deque", "d": "Tree", "answer": "b"},
        "What is the time complexity of binary search?": {"a": "O(n)", "b": "O(log n)", "c": "O(n^2)", "d": "O(1)", "answer": "b"},
        "What is the in-order traversal of a binary tree?": {"a": "Root-Left-Right", "b": "Left-Root-Right", "c": "Left-Right-Root", "d": "Right-Root-Left", "answer": "b"},
        "What is the maximum number of nodes in a binary tree with height h?": {"a": "2^h", "b": "2^(h+1) - 1", "c": "h^2", "d": "h + 1", "answer": "b"},
        "Which data structure is best for implementing a priority queue?": {"a": "Stack", "b": "Linked List", "c": "Heap", "d": "Hash Table", "answer": "c"},
        "Which traversal is Breadth-First Search (BFS) based on?": {"a": "Level Order", "b": "Depth Order", "c": "In-order", "d": "Post-order", "answer": "a"},
        "What is the time complexity of merge sort in the worst case?": {"a": "O(n^2)", "b": "O(n log n)", "c": "O(log n)", "d": "O(n)", "answer": "b"},
        "Which of the following sorting algorithms is in-place?": {"a": "Merge Sort", "b": "Bubble Sort", "c": "Radix Sort", "d": "Counting Sort", "answer": "b"},
        "What is the maximum degree of a node in a binary tree?": {"a": "1", "b": "2", "c": "3", "d": "Depends on the tree", "answer": "b"},
        "What is the space complexity of DFS for a graph?": {"a": "O(1)", "b": "O(V)", "c": "O(V + E)", "d": "O(V^2)", "answer": "b"},
        "Which data structure is used to implement recursion?": {"a": "Queue", "b": "Stack", "c": "Array", "d": "Linked List", "answer": "b"},
        "What is the height of a complete binary tree with n nodes?": {"a": "log(n)", "b": "log(n+1) - 1", "c": "log(n+1)", "d": "log(n-1)", "answer": "b"},
        "What is the primary purpose of a hash function?": {"a": "Sort data", "b": "Generate unique memory locations for data", "c": "Implement stacks", "d": "Traverse graphs", "answer": "b"},
        "Which data structure is ideal for solving the shortest path problem?": {"a": "Stack", "b": "Heap", "c": "Graph", "d": "Queue", "answer": "c"},
        "Which of the following is a divide and conquer algorithm?": {"a": "Quick Sort", "b": "Linear Search", "c": "Heap Sort", "d": "Bubble Sort", "answer": "a"},
    }
}

def load_data(file_path, default_data):
    if not os.path.exists(file_path):
        with open(file_path, "w") as file:
            json.dump(default_data, file)
    with open(file_path, "r") as file:
        return json.load(file)

def save_data(file_path, data):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

user_data = load_data(USER_DATA_FILE, {})
quiz_results = load_data(QUIZ_RESULTS_FILE, {})

def register():
    print("\n--- Register ---")
    username = input("Enter your username: ")
    if username in user_data:
        print("Username already exists. Please try again.")
        return
    password = getpass.getpass("Enter your password: ")
    email = input("Enter your email: ")
    enroll = input("Enter your Enrollment No.: ")
    TNP = input("Enter your TNP Batch No.:")
    user_data[username] = {"password": password, "email": email, "Enrollment No": enroll, "TNP Batch No.": TNP}
    
    print("Registration successfull !!!")

def login():
    print("\n--- Login ---")
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    if username in user_data and user_data[username]["password"] == password:
        print("Login successful!")
        return username
    else:
        print("Invalid username or password.")
        return None

def take_quiz(username):
    print(f"\nWelcome {username}! Choose a subject:")
    for i, subject in enumerate(questions.keys()):
        print(f"{i + 1}. {subject}")
    subject_choice = int(input("Enter your choice (1/2/3): "))
    subject = list(questions.keys())[subject_choice - 1]

    print(f"\nStarting {subject} Quiz!")
    score = 0
    for i, (question, options) in enumerate(questions[subject].items(), start=1):
        print(f"\nQ{i}: {question}")
        for key, option in options.items():
            if key != "answer":
                print(f"  {key}) {option}")
        user_answer = input("Enter your answer (a/b/c/d): ").lower()
        if user_answer == options["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! Correct answer is {options['answer']}) {options[options['answer']]}")

    percentage = (score / len(questions[subject])) * 100
    result = {"subject": subject, "score": score, "total": len(questions[subject]), "percentage": percentage}
    if username not in quiz_results:
        quiz_results[username] = []
    quiz_results[username].append(result)
    save_data(QUIZ_RESULTS_FILE, quiz_results)

    print(f"\nQuiz finished! Your score: {score}/{len(questions[subject])}")
    print(f"Percentage: {percentage:.2f}%")

def main():
    while True:
        print("!!! WELCOME TO THE QUIZ APPLICATION !!!")
        print("\n--- Main Menu ---")
        print("1. Register")
        print("2. Login")
        print("3. View Results")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            register()
        elif choice == "2":
            username = login()
            if username:
                take_quiz(username)
        elif choice == "3":
            print("\n--- Quiz Results ---")
            for user, results in quiz_results.items():
                print(f"\nUser: {user}")
                for result in results:
                    print(f"  Subject: {result['subject']}, Score: {result['score']}/{result['total']}, Percentage: {result['percentage']:.2f}%")
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


main()
