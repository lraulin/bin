#!/bin/python3

# Read a file
with open("/home/lee/.todo/inbox.txt", "rt") as in_file:
    text = in_file.read()
 
print(text)

