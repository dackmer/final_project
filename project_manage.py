# import database module
import csv, os


# define a funcion called initializing
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


class CSVTable:
    def __init__(self, file_path):
        self.file_path = file_path
        self.entries = []
        self.load_entries()
        self.evaluations = ProjectEvaluation()

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


class CSVDatabase:
    def __init__(self, database_name):
        self.database_name = database_name
        self.tables = {}

    def create_table(self, table_name, file_path):
        table = CSVTable(file_path)
        self.tables[table_name] = table


def initializing():
    file = CSVDatabase("MyCSVDatabase")

    # Define tables and corresponding CSV files
    tables_and_files = {
        "LoginTable": "login.csv",
        "PersonsTable": "persons.csv"
        # Add more tables as needed
    }

    for table_name, file_path in tables_and_files.items():
        file.create_table(table_name, file_path)

    return file


# here are things to do in this function:

# create an object to read all csv files that will serve as a persistent state for this program

# create all the corresponding tables for those csv files

# see the guide how many tables are needed

# add all these tables to the database


# define a function called login

def login(database):
    login_table = database.tables["LoginTable"]

    max_password_attempts = 3

    username = input("Enter your username: ")

    # Check if the entered username is valid
    if not any(i["username"] == username for i in login_table.entries):
        print("Invalid username.")
        return None

    # Allow three attempts for the password
    for _ in range(max_password_attempts):
        password = input("Enter your password: ")

        for i in login_table.entries:
            if i["username"] == username and i["password"] == password:
                print(f"Welcome! Your ID: {i['ID']}, Username: {i['username']}, Role: {i['role']}")
                return [i["ID"], i["role"]]

        print("Invalid password. Please try again.")

    print("sorry, limited password")
    return None


# here are things to do in this function:
# add code that performs a login task
# ask a user for a username and password
# returns [ID, role] if valid, otherwise returning None

# define a function called exit


def exit(database):
    for table in database.tables.values():
        table.save_to_csv()


# here are things to do in this function:
# write out all the tables that have been modified to the corresponding csv files
# By now, you know how to read in a csv file and transform it into a list of dictionaries.
# For this project, you also need to know how to do the reverse, i.e.,
# writing out to a csv file given a list of dictionaries. See the link below for a tutorial on how to do this:
# https://www.pythonforbeginners.com/basics/list-of-dictionaries-to-csv-in-python


# make calls to the initializing and login functions defined above

db = initializing()
val = login(db)

# Create a CSVTable within the CSVDatabase for persons
db.create_table("PersonsTable", "persons.csv")

# Access the CSVTable
persons_table = db.tables.get("PersonsTable")

# Check if persons_table is not None
if persons_table:
    # Now you can use persons_table
    new_entry = {"ID": "1234567", "fist": "New", "last": "Person", "type": "student"}
    persons_table.insert_entry(new_entry)
    persons_table.update_entry("ID", "1234567", "7654321")
    persons_table.save_to_csv()
    print(persons_table.entries)
else:
    print("PersonsTable not found.")
# based on the return value for login, activate the code that performs activities according to the role defined for
# that person_id

# based on the return value for login, activate the code that performs activities according to the role defined for that person_id

if val:
    user_id, role = val
    # if val[1] == 'admin':
    # see and do admin related activities
    if role == 'admin':
        print("admin role")
    # elif val[1] == 'student':
    # see and do student related activities
    elif role == 'student':
        print("student role")

        # Submit a project
        project_data = {"ID": user_id, "title": "My Project", "description": "Project description"}
        persons_table.insert_entry(project_data)
        print("Project submitted successfully.")

    # elif val[1] == 'member':
    # see and do member related activities
    elif role == 'member':
        print("member role")
    # elif val[1] == 'lead':
    # see and do lead related activities
    elif role == 'lead':
        print("lead role")
    # elif val[1] == 'faculty':
    # see and do faculty related activities
    elif role == 'faculty':
        print("faculty role")

        # Evaluate a project
        project_id_to_evaluate = input("Enter the project ID to evaluate: ")
        comments = input("Enter your comments: ")
        rating = input("Enter your rating: ")

        persons_table.evaluate_project(project_id_to_evaluate, user_id, comments, rating)
        print("Evaluation submitted successfully.")

        # Print project evaluations
        project_id_to_view = input("Enter the project ID to view evaluations: ")
        evaluations = persons_table.get_project_evaluations(project_id_to_view)

        if evaluations:
            print("Project Evaluations:")
            for eval in evaluations:
                print(f"Evaluator: {eval['evaluator_id']}, Comments: {eval['comments']}, Rating: {eval['rating']}")
        else:
            print("No evaluations found for the project.")

    # elif val[1] == 'advisor':
    # see and do advisor related activities
    elif role == 'advisor':
        print("advisor role")

# ...


# once everyhthing is done, make a call to the exit function
exit(db)
