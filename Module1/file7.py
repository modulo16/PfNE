from __future__ import unicode_literals, print_function

ip_addr1 = '192.168.1.1'
port1 = '80'
ip_addr2 = '192.168.2.1'
port2 = '443'
octets1 = ip_addr1.split(".")
octest2 = ip_addr2.split(".")

#Prints the Octets out to each formatted object by incrementing array elements
print ('\n')
print('-' * 80)
print(f"My IP Address is: {ip_addr1:20} {port1:^8}")
print(f"My IP Address is: {ip_addr2:20} {port2:^8}")
print('-' * 80)
print('\n')