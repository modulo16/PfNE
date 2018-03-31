from __future__ import print_function, unicode_literals

#Ensures Unicode is used for all strings.
my_str = 'whatever'
#Shows the String type, which should be unicode
type(my_str)

#declare string:
ip_addr = '192.168.1.1'
#check it with boolean:(True)
ip_addr == '192.168.1.1'
#(false)
ip_addr == '10.1.1.1'

#is this substring in this variable?
'192.168' in ip_addr


'1.1' in ip_addr


'15.1' not in ip_addr

#Strings also have indices starting at '0'
#in the case below we get '1' which is the first character
ip_addr[0]
#we can also get the last using negative notation. The follow gets the last:
ip_addr[-1]
#second to last:
ip_addr[-2]
#show length of string:
len(ip_addr)

#Example string concatenation
my_str = 'Hello'

my_str + ' something'


