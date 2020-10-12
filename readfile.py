from datetime import datetime
import time
import csv
import MySQLdb


starttime = datetime.now()
file_for_length = open("products.csv")
csvfile = open("products.csv","r")
reader = csv.reader(file_for_length)
lines = len(list(reader))
print ("Total line in file : "+str(lines))
count = 1
donesku = []

def AddToDatabase(sku,name,description):
    db = MySQLdb.connect(HOST,USR,PWD)
    c = db.cursor()
    c.execute("USE " + DBNAME)
    query = "INSERT INTO tablename (sku,name,description values ( \"%s\",\"%s\",\"%s\") ;" %(sku,name,description)
    c.execute(query)


for eachline in csvfile:
	lenth_of_line = len(eachline.strip().split(","))
	if lenth_of_line > 1 and eachline.strip().split(",")[1].lower() not in donesku:
		donesku.append(eachline.strip().split(",")[1].lower())
		description = ""
		name = eachline.strip().split(",")[0]
		sku = eachline.strip().split(",")[1]
		if lenth_of_line > 2:   
		    description = eachline.strip().split(",")[2]
		#time.sleep(1)    
		print ("Printing "+str(count)+" name : "+name)
		AddToDatabase(sku,name,description):
	count += 1
	if count > lines:
		break

endtime = datetime.now()
Total_time = endtime - starttime 
#print (Total_time)