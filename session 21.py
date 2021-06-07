def start(file):
    f=open(file,'r')
    data=f.read()
    word=input("Enter the word\n")
    print("1.Remove the word")
    print("2.Replace the word")
    i=int(input("Enter your choice\n"))
    if i==1:
        data=data.replace(word,'')
        print(data)
        f.close()
        f=open(file,'w')
        f.write(data)
        f.close()
    elif i==2:
        subs=input("Enter the word to be replaced\n")
        data=data.replace(word,subs)
        print(data)
        f.close()
        f=open(file,'w')
        f.write(data)
        f.close()

    else:
        print("Sorry you have entered a wrong number")
    
if __name__=='__main__':
    import os
    getFile=input("Enter the file name along with the extension\n")
    if os.path.exists(getFile):
        start(getFile)
    else:
        print("The file does not exists")
