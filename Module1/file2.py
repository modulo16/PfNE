from __future__ import print_function

#This is compatible in 2.7 and 3.6 with the Try Except:
try:
    ip_addr = raw_input("Enter an IP Address: ")
except NameError:
    ip_addr = input("Enter and Ip Address: ")
print(ip_addr)