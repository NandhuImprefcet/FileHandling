'''20	(Count words) Write a program that counts the number of words in President Abraham Lincoln’s
Gettysburg Address from 1861-Lincoln.txt		
'''

if __name__=='__main__':
    f=open("1861-Lincoln.txt",'r')
    data=f.read().split()
    count=0
    for i in data:
        if len(i)>0:
            count+=1
    print('No of words in the file is:',count)
