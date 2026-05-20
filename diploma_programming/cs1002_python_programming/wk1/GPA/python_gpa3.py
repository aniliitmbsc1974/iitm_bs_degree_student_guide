"""
Python_GPA3

Problem Statement: Accept a sequence of five single digit numbers separated by commas as input. Print the product of all five numbers.
"""

num=input("Enter 5 numbers separated by comma:")
prod=0;
d1=int(num[0])
d2=int(num[2])
d3=int(num[4])
d4=int(num[6])
d5=int(num[8])
prod= d1*d2*d3*d4*d5
print(prod)

"""Modified more generic for any digit number"""

num=input("Enter 5 numbers separated by comma:").split(",")
prod=0;
d1=int(num[0])
d2=int(num[1])
d3=int(num[2])
d4=int(num[3])
d5=int(num[4])
prod= d1*d2*d3*d4*d5
print(prod)