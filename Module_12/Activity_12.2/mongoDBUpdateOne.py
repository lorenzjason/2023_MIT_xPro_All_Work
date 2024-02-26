from pymongo import MongoClient


client = MongoClient('mongodb://localhost:27017')

db = client.EmployeeDB

employee = db.employee

filter = {"LastName":"Rose"}

newvalues = {"$set" : {'Age' : 32 } }

employee.update_one(filter, newvalues)


employeeCursor = employee.find()

for employee in employeeCursor:

    print(employee)