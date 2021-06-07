#Open a file in Write-Only Mode
f = open("test.txt" , "w")



f.write("This sentence is added in Write-Only mode.")
#data = f.read() #UnsupportedOperation: not readable
#close the file
f.close()
