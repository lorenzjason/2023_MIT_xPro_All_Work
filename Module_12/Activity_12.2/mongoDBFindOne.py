from pymongo import MongoClient


client = MongoClient('mongodb://localhost:27017')

db = client.EmployeeDB

employee = db.employee


employee = list(employee.find({"LastName":"Rigby"}))

print(employee)