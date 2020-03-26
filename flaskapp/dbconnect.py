import pymysql

def Cursor():
    db = pymysql.connect("remotemysql.com","P8fLcTUs68","JOx0xeTV8S","P8fLcTUs68",3306)
    cursor = db.cursor()
    return cursor

# prepare a cursor object using cursor() method
# cursor = db.cursor()

# cursor.execute("DESC main")

# # Uploading to database
# data = pd.read_csv("info.csv")
# for i in range(36):
# 	query = f"insert into main values ('{data.iloc[i][0]}', '{data.iloc[i][2]}', '{data.iloc[i][3]}', '{data.iloc[i][1]}', '{data.iloc[i][4]}', '{data.iloc[i][5]}')"
# 	print(query)
# 	cursor.execute(query)
# db.commit()

# data = cursor.fetchall()
# print(data)

