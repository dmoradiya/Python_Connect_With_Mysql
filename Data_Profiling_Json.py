import json
import pandas as pd
import pandas_profiling as pp
f = open("bank_db.json")
'''
data = json.load(f)
print(data["firstName"])
print(data["address"])
print(data["address"]["city"])
for x in data["phoneNumbers"]:
    print(x["type"])
'''
data_jason = json.load(f)
data = pd.DataFrame(data_jason) 
print(data)
profile = pp.ProfileReport(data) 
profile.to_file("output_bankdb.json")

