'''#open the file in read mode
f = open('test.txt', 'r')
d = f.read() #reads complete text
print(d)



f.close()



#open the file again in read mode
f = open('test.txt', 'r')



d = f.read(10) #reads 10 chars from beginning
print("First 10 chars: ", d)



f.close()



#open the file again in read mode
f = open('test.txt', 'r')
d = f.readline(15)
print("Frist 15 chars from line1: ", d)



d = f.readline(10)
print("next 10 chars from same line: ", d)



f.close()'''



#open the file again in read mode
f = open('test.txt', 'r')
data = f.readlines()
print("List of lines: ", data)



for line in data:
    print(line)



f.close()
