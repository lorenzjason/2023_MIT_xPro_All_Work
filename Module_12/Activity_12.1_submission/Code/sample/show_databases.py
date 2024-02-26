import mysql.connector
from datetime import datetime
import uuid
import sys
sys.dont_write_bytecode = True

cnx = mysql.connector.connect(user='root', 
    password= 'MyNewPass',
    host='localhost',
    port = '4999',
    database='',
    )

# create cursor
cursor = cnx.cursor()

# insert
query = ("SHOW DATABASES")
cursor.execute(query)

for row in cursor.fetchall():
    print(row)

# clean up
cursor.close()
cnx.close()    