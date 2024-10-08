# opening file in read mode 
with open('sales_data.csv','r') as df:
    reader=csv.DictReader(df)# dictreader method automatically reads the first row as header
    rows=list(reader)# preparing list to store all row data 
    jsondata=json.dumps(rows, indent=4)

with open('sales_data.json','w')as file:
    json_readable_file=file.write(jsondata)
    json_readable_file
    print("file created successfully")
    

    