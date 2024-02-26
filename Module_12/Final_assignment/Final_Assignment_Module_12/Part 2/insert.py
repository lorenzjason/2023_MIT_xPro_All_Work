import mysql.connector
import random
import sys
sys.dont_write_bytecode = True

cnx = mysql.connector.connect(user='root', 
    password='MyNewPass',
    host='127.0.0.1',
    database='Final',
    auth_plugin='mysql_native_password')

# create cursor
cursor = cnx.cursor()

# insert
id = random.randint(1,100)
multiply = id*3
plustwo= id+2
query1 = (f'INSERT INTO `Table1` VALUES("{id}","{multiply}","{plustwo}")')
cursor.execute(query1)

# clean up
cnx.commit()
cursor.close()
cnx.close()    