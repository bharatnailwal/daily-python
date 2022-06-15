# Importing the os library
import os
 
# The path for listing items
path = '.'
 
# The list of items
files = os.listdir(path)
 
# Loop to print each filename separately
for filename in files:
    print(filename)
