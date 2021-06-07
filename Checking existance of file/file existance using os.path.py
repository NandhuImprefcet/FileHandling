#How to check if file exists
#using os.path module
import os.path



#os.path.exist(filename): returns True if filename exist, otherwise False
print(os.path.exists("calc.txt"))



if os.path.exists("test4.txt") == True:
    print("File is already there.")
else:
    f = open("test4.txt", 'w')
    f.write("I have created test2.txt file just now")
    print("New file test2.txt is created!!!")
    f.close()
