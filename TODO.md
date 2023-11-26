# TODO List

## `project_manager.py`

### Initialization
- [ ] Create an object to read all CSV files.
- [ ] Create corresponding tables for those CSV files.
- [ ] Add all these tables to the database.

### Login
- [ ] Perform a login task.
- [ ] Ask the user for a username and password.
- [ ] Return [ID, role] if valid, otherwise return None.

### Activities Based on Role
- [ ] Activate code based on the role defined for that person_id.

### Exit
- [ ] Write out all the tables that have been modified to the corresponding CSV files.

## `database.py`

### CSVReader Class
- [ ] Read a CSV file and return its contents as a list of dictionaries.

### CSVTable Class
- [ ] Represent a table within the CSV database.
- [ ] Support loading entries, inserting entries, updating entries, and saving to CSV.

### CSVDatabase Class
- [ ] Represent a collection of CSV tables.
- [ ] Support creating tables within the database.

### Actions in __main__
- [ ] Create a CSVDatabase instance.
- [ ] Create a CSVTable within the CSVDatabase for persons.
- [ ] Access the CSVTable, insert an entry, update an entry, save changes to the CSV file, and print the updated entries.

this is how my code work or summary about it?

## `database.py`

CSVReader Class:
Purpose: Reads a CSV file and converts its contents into a list of dictionaries.

Explanation:
The CSVReader class has a constructor that takes the file path during initialization.
The read_csv method opens the file, reads it using csv.DictReader to interpret each row as a dictionary, and appends these dictionaries to the data list.

Summary: CSVReader provides a reusable component for reading CSV files and converting them into a structured format.

CSVTable Class:
Purpose: Represents a table within the CSV database and provides operations like loading entries, inserting entries, updating entries, and saving to CSV.

Explanation:
The CSVTable class has a constructor that takes the file path and initializes an empty list of entries.
The load_entries method uses a CSVReader instance to load entries from the CSV file.
insert_entry appends a new entry to the table.
update_entry updates an entry's value associated with a key.
save_to_csv writes the table's entries back to the CSV file.

Summary: CSVTable encapsulates operations related to a specific CSV file, providing a convenient way to interact with and manipulate data.

CSVDatabase Class:

Purpose: Represents a collection of CSV tables.

Explanation:
The CSVDatabase class has a constructor that takes a database name and initializes an empty dictionary of tables.
The create_table method creates a new CSVTable instance and adds it to the tables dictionary using the provided table name.

Summary: CSVDatabase manages multiple tables within the database, allowing for organization and separation of different data sets.

Actions in main:
Purpose: Demonstrates the usage of the classes defined above.
Explanation:
An instance of CSVDatabase (my_database) is created.
A CSVTable for persons is created within the database.
An entry is inserted into the persons table, updated, and changes are saved back to the CSV file.

Summary: The main section serves as an example of how to use the defined classes to perform operations on CSV data.

project_manager.py

Initialization Function:

Purpose: Creates an object to read all CSV files, creates corresponding tables, and adds them to the database.
Explanation:
The initializing function creates a CSVDatabase instance (file).
It defines tables and corresponding CSV files in a dictionary (tables_and_files).
A loop creates each table and adds it to the database.

Summary: The initialization function sets up the initial state of the database with tables and file associations.
Login Function:

Purpose: Performs a login task by checking a username and password against the login table.

Explanation:
The login function takes a database as input and prompts the user for a username and password.
It checks the validity of the entered username and password against the login table.
Returns [ID, role] if valid, otherwise returns None.

Summary: The login function provides a simple authentication mechanism by checking user credentials against a login table.

Activities Based on Role:
Purpose: Activates code based on the role defined for a user.

Explanation:
Based on the returned value from the login function, specific activities are activated for different roles (admin, student, member, lead, faculty, advisor).
Summary: The code segment demonstrates how different roles can trigger specific activities within the application.

Exit Function:

Purpose: Writes out all modified tables to the corresponding CSV files.

Explanation:
The exit function iterates through all tables in the database and saves any modifications back to the respective CSV files.

Summary: The exit function ensures that any changes made during the program's execution are persisted back to the CSV files.

Main Section:

Purpose: Demonstrates the overall flow of the application.

Explanation:
initializing and login functions are called to set up the database and authenticate the user.
Activities based on the user's role are performed.
Finally, the exit function is called to save any modifications made to the CSV files.

Summary: The main section orchestrates the overall functionality of the project manager, including initialization, user authentication, role-based activities, and data persistence.