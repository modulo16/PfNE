"""
Read the 'show_ip_bgp_summ.txt' file into your program.
From this BGP output obtain the first and last lines of the output.
From the first line use the string .split() method to obtain the local
AS number.
From the last line use the string .split() method to obtain the BGP peer IP address.
Print both local AS number and the BGP peer IP address to the screen.
"""
from __future__ import print_function, unicode_literals
from pprint import pprint
f = open("show_ip_bgp_summ.txt", mode = "r")
output = f.readlines()
first_line = output[0].split()
last_line = output[-1].split()
print(first_line[7])
print(last_line[0])
