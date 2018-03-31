"""
Create a list of five IP addresses.
Use the .append() method to add an IP address onto the end of the list. Use the .extend()
method to add two more IP addresses to the end of the list.
Use list concatenation to add two more IP addresses to the end of the list.
Print out the entire list of ip addresses. Print out the first IP address in the list. Print out the last IP address in
the list.
Using the .pop() method to remove the first IP address in the list and the last IP address in the list.
Update the new first IP address in the list to be '2.2.2.2'. Print out the new first IP address in the list.
"""
from __future__ import print_function, unicode_literals
ip_addrs = ['172.25.0.1', '172.25.16.1', '172.25.7.1', '172.25.23.1', '172.25.32.1']
ip_addrs.append('10.1.1.1')
ip_addrs = ip_addrs + ['192.168.1.1', '172.16.112.81']
print(ip_addrs[0])
print(ip_addrs[-1])
ip_addrs.pop(0)
ip_addrs[0] = '2.2.2.2'
print(ip_addrs[0])