f=open('full details.txt','r')
data=f.readlines()
for i in data:
    m=i.split('\t')
    print(len(m))
    
