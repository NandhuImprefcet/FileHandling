#Write only mode
f = open("test.txt", "w+")



data = f.read() #this wont give error
print("File Content: ", data)



f.write("Welcome to python programming")



#Where is my cursor?
position = f.tell()
print("Cursor Position is at: ", position)



#move cursor using seek() method
f.seek(10) #used to move at different position
position = f.tell() #returns current cursor location in number characters
print("Curson Position is at: ", position)



f.write(" OOPS")



data = f.read()
print("File content: ", data)



#close the file
f.close()
