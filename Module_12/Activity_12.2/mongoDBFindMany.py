from pymongo import MongoClient


client = MongoClient('mongodb://localhost:27017')

db = client.EmployeeDB

employee = db.employee



employeelist = employee.find({"LastName":"Smith"})
print(list(employeelist))
