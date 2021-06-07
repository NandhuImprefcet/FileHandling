'''(Write/read data) Write a program that writes 100 integers created randomly into a file. Integers are separated by a space in the file. Read the data back from the file and display the sorted data. Your program should prompt the user to enter a filename. If the file already exists, do not override it. Here is a sample run:
Enter a filename: test.txt
The file already exists
'''

if __name__=='__main__':
    import os
    s=input("Enter the file name along with the extension\n")
    if os.path.exists(s):
        print('The file already exists')
    else:
        import random
        f=open(s,'w')
        for i in range(100):
            a=random.randint(100,1000)
            string=str(a)+' '
            f.write(string)
        f.close()
        f=open(s,'r')
        data=f.read().split()
        datasort=[]
        for i in data:
            datasort.append(int(i))
        datasort.sort()
        for i in datasort:
            print(i,end=' ')
            
