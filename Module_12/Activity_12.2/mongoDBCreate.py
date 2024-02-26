from pymongo import MongoClient
from datetime import datetime
import uuid

client = MongoClient('mongodb://localhost:27017')


db = client.EmployeeDB


employee = db.employee

employee = [

                        {"FirstName":"John", "LastName":"Smith", "Age":25},

                        {"FirstName":"Peter", "LastName":"Smith", "Age":26},

                        {"FirstName":"Gabriel", "LastName":"Smith", "Age":28},

                        {"FirstName":"Penny", "LastName":"Lane", "Age":22},

                        {"FirstName":"Eleanor", "LastName":"Rigby", "Age":23},

                        {"FirstName":"Helen", "LastName":"Rose", "Age":23}

                     ]

if "EmployeeDB" in client.list_database_names():

    print("Employee database created!")

# insert document
insertion = db.employee.insert_many(employee)
print(insertion.inserted_ids)
