
#open a file:
f = open("show_version.txt")

#save text body to output variable:
output = f.read()
f.close()
#if we do that same f.read command again:
#f.read()
#we get back '', it's because we are at the end of the file now.
#we can start that the beginning again by doing:
#f.seek(0)
'''Seek usually doesn't matter because when we read files we usually inssue the f.close() call to close it.'''

#read contents of file line by line:
f.readline()
#all lines in one go show '\n' operators :
f.readlines()
#split the lines by newline('\n') operator
f.splitlines()

#proper Python:
with open("show_version.txt") as f:
    output = f.read()

#write operation:

f = open("new_file.txt", mode="w")
f.write("something\n")
#remebber to flush
f.flush()
#or you can use f.close()
#append operation would be f = open("new_file.txt", mode="a"
