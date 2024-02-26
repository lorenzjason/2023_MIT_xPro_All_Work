import mysql.connector
from datetime import datetime
import uuid
import sys
sys.dont_write_bytecode = True

cnx = mysql.connector.connect(user='root', 
    password='MyNewPass',
    host='127.0.0.1',
    database='restaurants',
    auth_plugin='mysql_native_password'
    )

# create cursor
cursor = cnx.cursor(buffered= True)


# insert
id = 1
time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
query = (f'INSERT INTO `posts` VALUES("{id}","{time}")')
cursor.execute(query)

# clean up
cnx.commit()
cursor.close()
cnx.close()    