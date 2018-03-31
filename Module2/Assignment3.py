"""
Read in the "show_arp.txt" file using the readlines() method. Use a list slice to remove the header line.

Use pretty print to print out the resulting list to the screen, syntax is:

from pprint import pprint
pprint(some_var)

Use the list .sort() method to sort the list based on IP addresses.

Create a new list slice that is only the first three ARP entries.

Use the .join() method to join these first three ARP entries back together as a single string using the newline
character ('\n') as the separator.

Write this string containing the three ARP entries out to a file named "arp_entries.txt".

"""
from __future__ import print_function, unicode_literals
from pprint import pprint
f = open("show_arp.txt", mode="r")
output = f.readlines()
output = output[1:]
pprint(output)

output.sort()
slice = output[0:3]
print(type(slice))
#pprint(slice)
input = "\n".join(slice)
pprint(input)
#input = output.join('\n')
w = open("arp_entries.txt", mode="w")
w.write(input)
w.flush()
w.close()


