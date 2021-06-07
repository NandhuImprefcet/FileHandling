#open a file in rb
#rb: opens a file for both reading and writing
f = open("test.txt", "rb")
data = f.read(6) #reads first five characteres
print("First 5 chars: ", data)



data = f.read(10)
print("next 10 chars: ", data)



data = f.read(10)
print("next 10 chars: ", data)



#writing something
#f.write("Welcome Writing")



f.close()
