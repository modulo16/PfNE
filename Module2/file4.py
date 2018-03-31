#Lists are Mutable:

my_list = ['hello', 'whatever']
id(my_list)
new_list = my_list
#making 2 variables point to same memory ID

new_list.append('something')
#the ID for new_list stays the same value in memory
#only Lists, and dictionaries are mutable
'''be careful when you are making copies of lists or dictionaries. 
This can bite you later on if you modify something you think you made a copy of but it's the original'''


