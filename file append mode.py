#Open a file in Write-Only Mode
f = open("test.txt" , "a")



f.write("\nThis sentence is added in Write-Only mode.")
#data = f.read() #UnsupportedOperation: not readable
#close the file
f.close()
f=open('test.txt','r')
data=f.read()
print(data)
