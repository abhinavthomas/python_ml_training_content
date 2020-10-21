x = open("cool2.txt", "r") # read mode
y = x.read() # read the whole
print(y)
# read file line by line
for line in x:
 line = line.replace("\n","")
 print(line)



x = open("cool.txt", "w") # write mode
x.write("SAP Labs\nBangalore\n")
x = open("cool.txt", "r") # read mode
y = x.read() # read the whole
print(y)
# read file line by line
for line in x:
 line = line.replace("\n","")
 print(line)
