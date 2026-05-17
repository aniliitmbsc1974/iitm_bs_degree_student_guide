# -*- coding: utf-8 -*-
"""
Python_PPA1


Problem Question: Print the first 5 positive integers in ascending order with one number in each line Note: Do not worry about "\\n" that comes at the end of the output. (using only print statement"
"""

print("******************************************")
print("This is printed using print statement only")
print("******************************************")

print(1)
print(2)
print(3)
print(4)
print(5)

"""
Modified Question:Print the first 5 positive integers in ascending order with one number in each line Note: Do not worry about "\n" that comes at the end of the output. (using for loop and print statement)"
"""

print("******************************************")
print("This is printed using for loop")
print("******************************************")
for i in range(1,6):
  print(i)

"""
range function has multiple variation
range(n) : it will take value from 0 to n-1
range(x,n): it will take value starting from x to n-1
range(x,n,s): it will take value starting from x to n-1 with step s
"""