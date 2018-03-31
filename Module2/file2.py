#python lists

#initialize variable to blank list
my_list = []
my_list = ['whatever', 22, 2.0]
#you do not need the same data type as elements in a list
my_list[0]
#'whatever'
#replace an index
my_list[2] = 'something'
len(my_list)
#3
#add elements:
my_list.append("hello")
#Add Multiple elements:
my_list.extend([2, 72])
#concatenate:
my_list + [2, 3, 'the']
#to keep concat in list:

my_list = my_list = [2, 3, 'the']
#pop the last element off the list:
my_list.pop()
#pop the first element off the list:
my_list.pop(0)
#you can also use del
del my_list[0]


