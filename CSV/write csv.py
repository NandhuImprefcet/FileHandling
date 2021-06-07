import csv
f = open("studentout.csv", "w")
writer = csv.writer(f)
writer.writerow(['Sno','Regno','Name','Age'])
writer.writerow(['1','2000080001','Raeksh','21'])
writer.writerow(['2','2000080002','Megha','20'])
writer.writerow(['3','2000080009','Siva','22'])
f.close()
