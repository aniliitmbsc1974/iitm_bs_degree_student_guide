"""
Python_PPA7


Problem Statement: Accept a five digit number as input and print the sum of its digits as output (without condition or loop).
For eg: 12345
1+2+3+4+5 =15
"""

num=input("Enter a five digit number:")
sum=int(num[0:1])
sum=sum+int(num[1:2])
sum=sum+int(num[2:3])
sum=sum+int(num[3:4])
sum=sum+int(num[4:5])
print(sum)

"""Alternate method with condition and loop"""

num=int(input("Enter a five digit number:"))
sum=0
if num >10000 and num <99999:
    while num>0:
        digit=num%10
        sum=sum+digit
        num=num//10
else:
    print("Invalid input")
print(sum)