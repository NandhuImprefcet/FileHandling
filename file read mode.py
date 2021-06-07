#Open a file in Read-Only Mode
f = open("test.txt", "r") #r->read only mode



#read the content
data = f.read()
print("File Content: ", data)



#close the file
f.close()
