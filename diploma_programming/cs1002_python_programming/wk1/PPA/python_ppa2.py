# -*- coding: utf-8 -*-
"""
Python_PPA2

Problem Statement: Print the following pattern.
*
**
***
****
*****

There are no spaces between consecutive stars. There are no spaces at the end of each line.
Note: Do not worry about the \n that you observe in the expected output. It can be ignored.
"""

print("*")
print("*"*2)
print("*"*3)
print("*"*4)
print("*"*5)

"""
Modified Statement: Print using the for Loop
"""

print("===========================")
print("print pattern using for loop")
print("============================")

for i in range(1,6):
  print("*"*i)