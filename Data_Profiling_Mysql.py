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

sql = "SELECT table_schema, table_name FROM information_schema.tables WHERE NOT (table_schema='sys' OR table_schema='phpmyadmin' OR table_schema='performance_schema' OR table_schema='mysql' OR table_schema='information_schema' OR table_schema='demo_capstone' OR table_schema='mvc_4point2' OR table_schema='mvc_library' OR table_schema='mvc_inventory')"

df = pd.read_sql(sql, mydb) 
df.to_json('list_of_tables.json')

#print('***************',df)

print('-------------',df)
df_len = len(df.index)
print(df_len)
df_array = []
for i in  df.index:
    
    if(i==(df_len-1)):
        df_array.append("SELECT"+" "+"count(*) as Row FROM "+df["table_name"][i])  
    else:
      df_array.append("SELECT"+" "+"count(*) as Row FROM "+df["table_name"][i]+" UNION ALL ")  
      


print(df_array)
join_df = "".join(df_array)
# for i in df_array:  
df_sql = pd.read_sql(join_df,mydb)
#   print(df_sql)
df_sql.to_json('table.json')

#df_keys = pd.read_sql("show index.Key_name from transaction",mydb)
#print(df_keys['Key_name'])
#print(len(df_keys['Key_name']))