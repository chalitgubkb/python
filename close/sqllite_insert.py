import sqlite3
import os

os.system('cls')

db = sqlite3.connect('dbphuket.db')
sql="insert into users values(null,'Bhurisub','Dejpipatpracha','m')"
db.execute(sql)
db.commit()

print("เพิ่มได้แล้วครับ")
db.close()