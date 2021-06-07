#How to check if file exists
#through exception handling
try:
    f = open("sample.txt", "r")
    print("File Exist")
    print(f.read())
except IOError:
    print("File does not Exist")
    f = open("sample.txt", "w")
    f.write("I have just now create this file.")
    print("sample.txt is created")
finally:
    f.close()
