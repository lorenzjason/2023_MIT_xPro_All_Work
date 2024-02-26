from pymongo import MongoClient


client = MongoClient('mongodb://localhost:27017')

db = client.EmployeeDB

employee = db.employee

filter = {'LastName':'Smith'}

newvalues = { "$set": { 'Department': 'Computer Science' } }

employee.update_many(filter, newvalues)

employeeCursor = employee.find()

for employee in employeeCursor:

    print(employee)