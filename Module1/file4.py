from __future__ import print_function, unicode_literals
#how to declare strings with quotes"
mystr1 = 'whatever'
mystr2 = "something else"
mystr3 = '''
This string
can span
multiple lines
using triple quote
'''

print(mystr1)
print(mystr2)
print(mystr3)

#print what the string looks like to python interpreter:
print(repr(mystr3))
#output: '\nThis string\ncan span\nmultiple lines\nusing triple quote\n'
#this can help with troubleshooting strings when you are getting something unexpected.

#one method that is helpful
#This variable has a bunch of whitespace:
my_str = '     whatever, something else\n\n\n'

#Strips off all the whitespace
my_str.strip()
#strips off the leading whitespace:
my_str.lstrip()
#strips off trailing whitespace:
my_str.rstrip()

ip_addr = '192.168.1.1'
#splits the string at the period
ip_addr.split(".")


