#How to write a csv file
import csv



f = open("studentout1.csv", "w")
writer = csv.writer(f)



#writing list of rows at a time
rows = [['Sno', 'Regno', 'Name', 'Age'],
['1', '2000080001', 'Rakesh', '21'],
['2', '2000080002', 'Megha', '20'],
['3', '2000080009', 'Siva', '22'],
['1', '2000080001', 'Rakesh', '21'],
['2', '2000080002', 'Megha', '20'],
['3', '2000080009', 'Siva', '22']]



writer.writerows(rows)



f.close()

