import csv


class ProjectEvaluation:
    def __init__(self):
        self.evaluations = []

    def add_evaluation(self, project_id, evaluator_id, comments, rating):
        evaluation = {
            "project_id": project_id,
            "evaluator_id": evaluator_id,
            "comments": comments,
            "rating": rating
        }
        self.evaluations.append(evaluation)

    def get_evaluations_for_project(self, project_id):
        return [eval for eval in self.evaluations if eval["project_id"] == project_id]


class CSVReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_csv(self):
        data = []
        with open(self.file_path) as f:
            rows = csv.DictReader(f)
            for r in rows:
                data.append(dict(r))
        return data


class AdvisorPendingRequestTable:
    def __init__(self, file_path):
        self.file_path = file_path
        self.entries = []
        self.load_entries()

    def load_entries(self):
        csv_reader = CSVReader(self.file_path)
        self.entries = csv_reader.read_csv()

    def insert_request(self, project_id, to_be_advisor):
        request = {
            "ProjectID": project_id,
            "to_be_advisor": to_be_advisor,
            "Response": "",
            "Response_date": ""
        }
        self.entries.append(request)

    def update_request_response(self, project_id, to_be_advisor, response, response_date):
        for entry in self.entries:
            if entry["ProjectID"] == project_id and entry["to_be_advisor"] == to_be_advisor:
                entry["Response"] = response
                entry["Response_date"] = response_date

    def save_to_csv(self):
        with open(self.file_path, mode='w', newline='') as f:
            fieldnames = self.entries[0].keys() if self.entries else []
            writer = csv.DictWriter(f, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(self.entries)


class CSVTable:
    def __init__(self, file_path):
        self.file_path = file_path
        self.entries = []
        self.load_entries()
        self.evaluations = ProjectEvaluation()
        self.advisor_pending_requests = AdvisorPendingRequestTable("advisor_pending_requests.csv")

    def load_entries(self):
        csv_reader = CSVReader(self.file_path)
        self.entries = csv_reader.read_csv()

    def insert_entry(self, entry):
        self.entries.append(entry)

    def update_entry(self, key, old_value, new_value):
        for i in self.entries:
            if i.get(key) == old_value:
                i[key] = new_value

    def save_to_csv(self):
        with open(self.file_path, mode='w', newline='') as f:
            fieldnames = self.entries[0].keys() if self.entries else []
            writer = csv.DictWriter(f, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(self.entries)

    def evaluate_project(self, project_id, evaluator_id, comments, rating):
        self.evaluations.add_evaluation(project_id, evaluator_id, comments, rating)

    def get_project_evaluations(self, project_id):
        return self.evaluations.get_evaluations_for_project(project_id)

    def insert_advisor_request(self, project_id, to_be_advisor):
        self.advisor_pending_requests.insert_request(project_id, to_be_advisor)

    def update_advisor_request_response(self, project_id, to_be_advisor, response, response_date):
        self.advisor_pending_requests.update_request_response(project_id, to_be_advisor, response, response_date)

    def view_advisor_requests(self):
        for request in self.advisor_pending_requests.entries:
            print(f"ProjectID: {request['ProjectID']}, to_be_advisor: {request['to_be_advisor']}, "
                  f"Response: {request['Response']}, Response_date: {request['Response_date']}")


class CSVDatabase:
    def __init__(self, database_name):
        self.database_name = database_name
        self.tables = {}

    def create_table(self, table_name, file_path):
        table = CSVTable(file_path)
        self.tables[table_name] = table


def initializing():
    file = CSVDatabase("MyCSVDatabase")

    tables_and_files = {
        "LoginTable": "login.csv",
        "PersonsTable": "persons.csv"
        # Add more tables as needed
    }

    for table_name, file_path in tables_and_files.items():
        file.create_table(table_name, file_path)

    return file


def login(database):
    login_table = database.tables["LoginTable"]

    max_password_attempts = 3

    username = input("Enter your username: ")

    if not any(i["username"] == username for i in login_table.entries):
        print("Invalid username.")
        return None

    for attempt in range(1, max_password_attempts + 1):
        password = input("Enter your password: ")

        for user_info in login_table.entries:
            if user_info["username"] == username and user_info["password"] == password:
                print(
                    f"Welcome! Your ID: {user_info['ID']}, Username: {user_info['username']}, Role: {user_info['role']}")
                return user_info["ID"], user_info["role"]

        if attempt < max_password_attempts:
            print("Invalid password. Please try again.")
        else:
            print("Sorry, limited password attempts reached.")
            return None, None


def exit(database):
    for table in database.tables.values():
        table.save_to_csv()


def show_user_info(database):
    login_table = database.tables["LoginTable"]
    for user_info in login_table.entries:
        print(f"ID: {user_info['ID']}, Username: {user_info['username']}")


def add_user(database):
    login_table = database.tables["LoginTable"]
    new_username = input("Enter new username: ")
    new_password = input("Enter new password: ")
    new_role = input("Enter new role: ")
    new_id = input("Enter new ID: ")

    new_user = {"ID": new_id, "username": new_username, "password": new_password, "role": new_role}
    login_table.insert_entry(new_user)
    login_table.save_to_csv()
    print("User added successfully.")


def delete_user(database):
    login_table = database.tables["LoginTable"]
    username_to_delete = input("Enter the username to delete: ")

    if any(i["username"] == username_to_delete for i in login_table.entries):
        login_table.entries = [i for i in login_table.entries if i["username"] != username_to_delete]
        login_table.save_to_csv()
        print(f"User '{username_to_delete}' deleted successfully.")
    else:
        print("User not found.")


def menu(database):
    while True:
        print("\nMenu:")
        print("1. View Usernames and IDs")
        print("2. Add User (Admin Only)")
        print("3. Delete User (Admin Only)")
        print("4. View Advisor Pending Requests (Admin Only)")
        print("5. Respond to Advisor Requests (Admin Only)")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            show_user_info(database)
        elif choice == "2":
            add_user(database)
        elif choice == "3":
            delete_user(database)
        elif choice == "4":
            database.tables["PersonsTable"].view_advisor_requests()
        elif choice == "5":
            database.tables["PersonsTable"].update_advisor_request_response()
        elif choice == "6":
            exit(database)
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


# Example usage
db = initializing()
val = login(db)

if val:
    user_id, role = val

    if role == 'admin':
        print("admin role")
        menu(db)
    elif role == 'student':
        print("student role")

        persons_table = db.tables.get("PersonsTable")

        if persons_table:
            new_entry = {"ID": "1234567", "fist": "New", "last": "Person", "type": "student"}
            persons_table.insert_entry(new_entry)
            persons_table.update_entry("ID", "1234567", "7654321")
            persons_table.save_to_csv()
            print(persons_table.entries)
        else:
            print("PersonsTable not found.")

    elif role == 'member':
        print("member role")
    elif role == 'lead':
        print("lead role")
    elif role == 'faculty':
        print("faculty role")

        persons_table = db.tables.get("PersonsTable")

        if persons_table:
            project_id_to_evaluate = input("Enter the project ID to evaluate: ")
            comments = input("Enter your comments: ")
            rating = input("Enter your rating: ")

            persons_table.evaluate_project(project_id_to_evaluate, user_id, comments, rating)
            print("Evaluation submitted successfully.")

            project_id_to_view = input("Enter the project ID to view evaluations: ")
            evaluations = persons_table.get_project_evaluations(project_id_to_view)

            if evaluations:
                print("Project Evaluations:")
                for eval in evaluations:
                    print(f"Evaluator: {eval['evaluator_id']}, Comments: {eval['comments']}, Rating: {eval['rating']}")
