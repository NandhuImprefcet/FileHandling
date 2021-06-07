f=open('test.txt','rb')
for i in range(5):
    data=f.read(15)
    print(data)
