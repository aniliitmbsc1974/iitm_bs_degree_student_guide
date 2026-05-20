"""
Python_GPA5


Problem Statement: Accept two positive integers x and y as input. Print the number of digits in x**y. You should be able to solve this problem using the concepts covered in week-1.
"""

x= input("Enter the number:")
y= input("Enter the power:")
val= int(x)**int(y)
num_digit=len(str(val))
print(num_digit)