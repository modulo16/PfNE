"""Prompt a user to enter in an IP address from standard input. Read the IP address in and break it up into its octets. Print out the octets in decimal, binary, and hex.

Your program output should look like the following:

 $ python exercise2.py
Please enter an IP address: 80.98.100.240

    Octet1         Octet2         Octet3         Octet4
------------------------------------------------------------
      80             98             100            240
   0b1010000      0b1100010      0b1100100     0b11110000
     0x50           0x62           0x64           0xf0
------------------------------------------------------------

Four columns, fifteen characters wide, a header column, data centered in the column"""
from __future__ import print_function, unicode_literals

ip_addr = input("Please enter an IP address: ")
octets = ip_addr.split('.')
int_octets1 = int(octets[0])
int_octets2 = int(octets[1])
int_octets3 = int(octets[2])
int_octets4 = int(octets[3])
print ('\n')
print ("{:^15}{:^15}{:^15}{:^15}".format("Octet1", "Octet2", "Octet3", "Octet4"))
print ('-' * 80)
print ("{:^15}{:^15}{:^15}{:^15}".format(*octets))
print ("{:^15}{:^15}{:^15}{:^15}".format(bin(int_octets1), bin(int_octets2), bin(int_octets3), bin(int_octets4)))
print ("{:^15}{:^15}{:^15}{:^15}".format(hex(int_octets1), hex(int_octets2), hex(int_octets3), hex(int_octets4)))
print ('-' * 80)
