import mysql.connector
import pandas as pd
import pandas_profiling as pp 
import sys
import json

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  port="3306",
  database="bank_db"
)
mycursor = mydb.cursor()
sql = "SELECT table_schema, table_name FROM information_schema.tables WHERE NOT (table_schema='sys' OR table_schema='phpmyadmin' OR table_schema='performance_schema' OR table_schema='mysql' OR table_schema='information_schema')"
#mycursor.execute(sql)
#data = pd.DataFrame(mycursor)
df = pd.read_sql(sql, mydb) 
df.to_json('list_of_tables.json')

print(df)
print(len(df))
