'''15	Write a program that removes all the occurrences of a specified string from a text file. Your program should prompt the user to enter a filename and a string to be removed. Here is a sample run:
Enter a filename: test.txt
Enter the string to be removed: morning	'''	

def start(file):
    f=open(file,'r')
    data=f.read()
    word=input("Enter the word\n")
    data=data.replace(word,'')
    f.close()
    f=open(file,'w')
    f.write(data)
    f.close()

if __name__=='__main__':
    import os
    getFile=input("Enter the file name along with the extension\n")
    if os.path.exists(getFile):
        start(getFile)
    else:
        print("The file does not exists")

