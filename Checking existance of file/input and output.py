
#open input.txt file in read mode
f = open('input.txt', 'r')
data = f.read()
a, b = data.split()
a, b = int(a), int(b)
f.close()
s = a + b



#create a new file with name output.txt
outf = open('output.txt', 'w')
outf.write(str(s))
outf.close()

