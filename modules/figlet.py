import sys

from pyfiglet import figlet_format

def figgletizer(input):
    return(figlet_format(input))

print("running")
print(figgletizer("test"))