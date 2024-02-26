# pip install redis
import redis
from datetime import datetime

# connect to server
re = redis.Redis(host='localhost', port=6379, db=0)

r= {'Milk':"Lactose", "Bread":"Gluten"}

re.mset(r)