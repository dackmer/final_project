# try wrapping the code below that reads a persons.csv file in a class and make it more general such that it can read in any csv file

import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


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

# add in code for a Database class
class CSVTable:
    def __init__(self, file_path):
        self.file_path = file_path
        self.entries = []
        self.load_entries()

    def load_entries(self):
        csv_reader = CSVReader(self.file_path)
        self.entries = csv_reader.read_csv()

    def insert_entry(self, entry):
        self.entries.append(entry)

    def update_entry(self, key, old_value, new_value):
        for entry in self.entries:
            if entry.get(key) == old_value:
                entry[key] = new_value

    def save_to_csv(self):
        with open(self.file_path, mode='w', newline='') as f:
            fieldnames = self.entries[0].keys() if self.entries else []
            writer = csv.DictWriter(f, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(self.entries)

# add in code for a Table class


class CSVDatabase:
    def __init__(self, database_name):
        self.database_name = database_name
        self.tables = {}

    def create_table(self, table_name, file_path):
        table = CSVTable(file_path)
        self.tables[table_name] = table

# modify the code in the Table class so that it supports the insert operation where an entry can be added to a list of dictionary

# modify the code in the Table class so that it supports the update operation where an entry's value associated with a key can be updated

my_database = CSVDatabase("MyCSVDatabase")

# Create a CSVTable within the CSVDatabase for persons
my_database.create_table("PersonsTable", "persons.csv")

# Access the CSVTable
persons_table = my_database.tables["PersonsTable"]

# Insert an entry
new_entry = {"ID": "1234567", "fist": "New", "last": "Person", "type": "student"}
persons_table.insert_entry(new_entry)

# Update an entry
persons_table.update_entry("ID", "1234567", "7654321")

# Save changes to the CSV file
persons_table.save_to_csv()

# Print the updated entries
print(persons_table.entries)