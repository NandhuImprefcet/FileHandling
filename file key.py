#before writing anything in binary form use b as prefix else it will be taken as
#number or string only not in binary form.

#r: Read-Only mode, opens a file only for reading
f = open("test.txt", "r")
##only reads the data writeable file not supported


#r+: opens a file for both reading and writing
f = open("test.txt", "r+")
##read and writes data at the eof when writen f.write but when added with
##f.seek() it overwrites the data


#rb: opens a file for reading binary file
f = open("test.txt", "rb")
##cannot write data works just like r mode but reads in binary type


#rb+: opens a file for both reading and writing a binary file
f=open('test.txt','rb+')
##addition of rb and r+ is rb+

###write function itself overwrites the data only irrespective of the mode
###in which it has been opened


#w: Write-Only mode, opens a file only for writing
f = open("test.txt", "w")
##over-writes all the things which was present in it



#w+: opens a file for both writing and reading
f = open("test.txt", "w+")
##on the call of the mode itself it over-writes the data present in it
##it is better to make sure that we use new file to it because it doesn't give
##any error when file not found


#wb: opens a file for writing binary file
f = open("test.txt", "wb")
##it does not support reading but it overwrites the previous existing data and
##new data can be writen using b as a prefix to it


#wb+; opens a file for both writing and reading binary file
f = open("test.txt", "wb+")
##it is the combination of wb and w+ mode we can write and read in this mode
##the main difference between this w+ and r+ is that, r+ does not overwrite
##during the fnctiion call but w+ overwrites everything and makes it as a null
##file and then starts writing the statement



#a: opens a file in append mode for appending content, and position the cursor at the EOF
f = open("test.txt", "a")
##it does not read file but adds line at EOF, this works like a write mode without
##over-writing the content in it and also only we can add it to end of the statement




#a+: opens a file in both append and read and write mode
f = open("test.txt", "a+")
##inspite of trying to add smth in the first line using seek() function
##it gets added to only at the eof only



#ab: opens a file in append mode for appending binary content
f = open("test.txt", "ab")
##a in appending lines in binary form


#ab+: opens a file in both appending reading and writing
f = open("test.txt", "ab+")
##append mode in read format in binary form is this ab+ mode
