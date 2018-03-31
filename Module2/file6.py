#Joins and sys.argv
#ex:

ipv6 = '2001:0db8:85a3:0000:8a2e:0370:7334'
ipv6.split(":")
words = ipv6.split(":")
type(words)

":".join(words)

# another example:

ip1 = "192.168.1.1"
ip1.split('.')
octets = ip1.split('.')
".".join(octets)

