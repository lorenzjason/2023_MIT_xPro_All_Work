import mysql.connector

def insertMBTARecord(mbtaList):
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="MyNewPass",
    database="MBTAdb"
    )

    mycursor = mydb.cursor()
    #complete the following line to add all the fields from the table
    sql = "insert into mbta_buses ( id, longitude, latitude, current_status, bearing, current_stop_sequence, direction_id, label) values (%s, %s,%s, %s, %s,%s, %s, %s)"
    for mbtaDict in mbtaList:
        #complete the following line to add all the fields from the table
        val = (mbtaDict['id'], mbtaDict['latitude'], mbtaDict['longitude'], mbtaDict['current_status'], mbtaDict['bearing'], mbtaDict['current_stop_sequence'], mbtaDict['direction_id'], mbtaDict['label'])
        mycursor.execute(sql, val)

    mydb.commit()