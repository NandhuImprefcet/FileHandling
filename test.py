#How to read a text file from Hard Disk
#test.txt file is already there in current dir
fileObj = open("test.txt")






'''FileNotFoundError:
[Errno 2] No such file or directory: 'test1.txt'
'''



#read a file content
data = fileObj.read()
print("File Content: ", data)
print('\n\n')
print(open('../test.txt').read())
print('\n\n')
print(open('In/test.txt').read())


#close the file
fileObj.close()
