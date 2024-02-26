from pymongo import MongoClient


client = MongoClient('mongodb://localhost:27017')

db = client.EmployeeDB

employee = db.employee

filter = {"LastName":"Smith"}

employee.delete_many(filter)

employeeCursor = employee.find()

for employee in employeeCursor:

    print(employee)