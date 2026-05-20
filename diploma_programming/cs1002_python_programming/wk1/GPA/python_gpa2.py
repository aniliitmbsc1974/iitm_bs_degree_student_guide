"""
Python_GPA2

Problem Statement: Accept the date in DD-MM-YYYY format as input and print the year as output.
"""

datestring=input("Enter the date in DD-MM-YYYY format")
Day=datestring[:2]
Month=datestring[3:4]
Year=datestring[-4:]
print("The year is",Year)