"""You have the following three variables from the arp table of a router:

mac1 = "Internet  10.220.88.29           94   5254.abbe.5b7b  ARPA   FastEthernet4"
mac2 = "Internet  10.220.88.30            3   5254.ab71.e119  ARPA   FastEthernet4"
mac3 = "Internet  10.220.88.32          231   5254.abc7.26aa  ARPA   FastEthernet4"

Process these ARP entries and print out a table of "IP ADDR" to "MAC ADDRESS" mappings. The output should look like following:

             IP ADDR          MAC ADDRESS
-------------------- --------------------
        10.220.88.29       5254.abbe.5b7b
        10.220.88.30       5254.ab71.e119
        10.220.88.32       5254.abc7.26aa

Two columns, 20 characters wide, data right aligned, a header column."""
from __future__ import print_function, unicode_literals
Mac1 = "Internet  10.220.88.29           94   5254.abbe.5b7b  ARPA   FastEthernet4"
Mac2 = "Internet  10.220.88.30            3   5254.ab71.e119  ARPA   FastEthernet4"
Mac3 = "Internet  10.220.88.32          231   5254.abc7.26aa  ARPA   FastEthernet4"

#Testing purposes:
#print(repr(mac1))
Entities1 = Mac1.split()
Entities2 = Mac2.split()
Entities3 = Mac3.split()
Banner = "-" * 20
print("\n")
print("{:>20}{:>20}".format("IP ADDR", "MAC ADDRESS"))
print("{:>20}{:>20}".format(Banner,Banner))
print("{:>20}{:>20}".format(Entities1[1],Entities1[3]))
print("{:>20}{:>20}".format(Entities2[1],Entities2[3]))
print("{:>20}{:>20}".format(Entities3[1],Entities3[3]))