import pymysql

db = pymysql.connect("remotemysql.com","P8fLcTUs68","JOx0xeTV8S","P8fLcTUs68",3306)

# prepare a cursor object using cursor() method
cursor = db.cursor()

cursor.execute("DESC main")

data = cursor.fetchall()

print(data)

