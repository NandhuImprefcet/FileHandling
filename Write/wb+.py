#methods of write content in file
#1. file.write(string)
f = open('test1.txt', 'w')
f.write("We have erased the previous content")



f.close()
#2. file.writelines(stringlist)
f = open('test1.txt', 'w')
f.writelines(["Hello\t", "Welcome\n", "To\n", "Python\n", "Programming."])



f.close()
f=open('test1.txt','r')
print(f.read())
