"""
Python_GPA1.ipynb

Problem Statement: Accept five words as input and print the sentence formed by these words after adding a space between consecutive words and a full stop at the end. (without using condition or loop)
"""

word1=str(input("Enter the first word: "))
word2=str(input("Enter the second word: "))
word3=str(input("Enter the third word: "))
word4=str(input("Enter the fourth word: "))
word5=str(input("Enter the fifth word: "))
space=" "
stop="."
sentence=word1+space+word2+space+word3+space+word4+space+word5+stop
print(sentence)

"""Modified solution with loop and contitions"""

sentence=""
for i in range(5):
  word=""
  word=str(input("Enter the word "+str(i+1)+": " ))
  sentence+=word
  if i==4:
    sentence+="."
  else:
    sentence+=" "
print(sentence)