from pymongo import MongoClient


client = MongoClient('mongodb://localhost:27017')

db = client.EmployeeDB

employee = db.employee

filter = {"LastName":"Rose"}

employee.delete_one(filter)

employeeCursor = employee.find()

for employee in employeeCursor:

    print(employee)