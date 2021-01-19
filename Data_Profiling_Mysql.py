import mysql.connector
import pandas as pd
import pandas_profiling as pp 
import sys

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  port="3306",
  database="bank_db"
)
mycursor = mydb.cursor()
sql = "show index from transaction "
#mycursor.execute(sql)
#data = pd.DataFrame(mycursor)
df = pd.read_sql(sql, mydb) 

print(df)
print(len(df))
#print(data)
#print(mycursor.rowcount)
#profile = pp.ProfileReport(df) 
#profile.to_file("output.json")
#num_fields = mycursor.description
#print(num_fields)
#field_names = [i[0] for i in mycursor.description]
#print(field_names)