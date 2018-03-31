#List Slices
f = open("show_version.txt")
output = f.readlines()

type(output)
#list
len(output)
58
#slicing first through the 4th line of the file but doesn't include 5
output[0:5]
#or leaving left value balnk starts at 0
output[:5]
#leaving right value blank goes all the way to the end of the list:
output[55:]
#another example
output[27:31]
#this allows us to parse existing lists to create new lists


