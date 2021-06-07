#import csv module
import csv



#read the file in r mode
f = open("student.csv", "r")
readercsv = csv.reader(f)



#iterate the content
for line in readercsv:
    print(line)
