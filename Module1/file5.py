from __future__ import print_function, unicode_literals

ip_addr1 = '172.16.1.1'
ip_addr2 = '172.31.17.99'
ip_addr3 = '217.88.17.1'


#making a banner:
print ("\n")
print("-" * 80)
#print ("\n")
print(ip_addr1, ip_addr2, ip_addr3)
print("\n")

#Better way:
print ("\n")
print("-" * 80)
#print ("\n")
print("{}{}{}".format(ip_addr1, ip_addr2, ip_addr3))
print("\n")


#Better way, with column formatted left aligned:
print ("\n")
print("-" * 80)
#print ("\n")
print("{:<20}{:<20}{:<20}".format(ip_addr1, ip_addr2, ip_addr3))
print("\n")

#Better way, with column formatted left aligned:
print ("\n")
print("-" * 80)
#print ("\n")
print("{:>20}{:>20}{:>20}".format(ip_addr1, ip_addr2, ip_addr3))
print("\n")

#Better way, with column formatted centered:
print ("\n")
print("-" * 80)
#print ("\n")
print("{:^20}{:^20}{:^20}".format(ip_addr1, ip_addr2, ip_addr3))
print("-" * 80)
print("\n")

#Better way, with column formatted centered, and name arguments for format argument list.:
print ("\n")
print("-" * 80)
#print ("\n")
print("{my_ip:^20}{ip:^20}{ip_alt:^20}".format(my_ip=ip_addr1, ip=ip_addr2, ip_alt=ip_addr3))
print("-" * 80)
print("\n")