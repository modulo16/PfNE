#Tuples: Lists you can't modify (immutable)

my_tuple = (2, 'whatever', 22.0)
type(my_tuple)
#tuple
#you can use list operators like:
my_tuple[0]
#2
my_tuple[-1]
#22.0
#you cannot modify i.e my_tuple.append(), this will error
#Yu can create lists out of tuples though, and then modify them further!
my_list = my_tuple
my_list = list(my_list)


