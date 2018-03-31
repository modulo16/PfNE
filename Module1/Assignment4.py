"""4. Create a show_version variable that contains the following

 show_version = "*0        CISCO881-SEC-K9       FTX0000038X    "

Remove all leading and trailing whitespace from the string.

Split the string and extract the model and serial_number from it.

Check if 'Cisco' is contained in the model string (ignore capitalization).

Check if '881' is in the model string.

Print out both the serial number and the model.
"""

from __future__ import print_function, unicode_literals

show_version = "*0        CISCO881-SEC-K9       FTX0000038X    "
show_version = show_version.strip()
print(repr(show_version))
print(show_version)
entities = show_version.split()

model = entities[1]
serial_number = entities[2]

print(model)
print(serial_number)

print("Cisco".casefold() in model.casefold())
print("881" in model)
