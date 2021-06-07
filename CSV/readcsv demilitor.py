#import csv module
import csv#read the file in r mode
f = open("students.txt", "r")
#csv.reader() takes delimiter
readercsv = csv.reader(f, delimiter='\t')#iterate the content
for line in readercsv:
    print(line)

