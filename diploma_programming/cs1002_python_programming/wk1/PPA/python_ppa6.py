"""
Python_PPA6


Problem Statement: Accept the registration number of a vehicle as input and print its state-code as output.
Example: If Vehicle number is "TN-10-AB-2010", print "TN"
"""

vehicle_no=input("Enter the registration number: ")
state_code= vehicle_no[0:2]
print(state_code)