#How to check if file exists
#using pathlib package Path module
from pathlib import Path
filename = "test7.txt"
pathObj = Path(filename)
print(filename,"exist?",pathObj.is_file())
if pathObj.is_file() == True:
    f = open(filename, "r")
    print(f.read())
    f.close()
else:
    f = open(filename, "w")
    f.write("Hello, Welcome to Python Programming")
    f.close()
