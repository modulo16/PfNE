from __future__ import unicode_literals, print_function

ip_addr = '192.168.1.1'
octets = ip_addr.split(".")

#Prints the Octets out to each formatted object by incrementing array elements
print ('\n')
print('-' * 80)
print("{:10}{:10}{:10}{:10}".format(octets[0], octets[1], octets[2], octets[3]))
print('-' * 80)
print('\n')

#This is the better way, the star says that this is a sequence of elements that corresponds to the the 4 values:
print ('\n')
print('-' * 80)
print("{:10}{:10}{:10}{:10}".format(*octets))
print('-' * 80)
print('\n')


