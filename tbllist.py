import sqlite3

con = sqlite3.connect('db.sqlite3')

cursorObj = con.cursor()

cursorObj.execute('SELECT name from sqlite_master where type= "table"')

print(cursorObj.fetchall())