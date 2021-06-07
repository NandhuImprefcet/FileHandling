'''(Replace text) Write a program that replaces text in a file. Your program should prompt the user to enter a filename, an old string, and a new string. Here is a sample run:
Enter a filename: test.txt
Enter the old string to be replaced: morning
Enter the new string to replace the old string: 
afternoon
'''


def start(file):
    f=open(file,'r')
    data=f.read()
    word=input("Enter the word\n")
    subs=input("Enter the word to be replaced\n")
    data=data.replace(word,subs)
    print(data)
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
