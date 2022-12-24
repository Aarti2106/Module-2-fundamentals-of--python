#Write a python program to count the number of characters(character frequency)in string.

s=input("Enter string:")
ch=0
n=0
for i in s:
    if i.isalpha():
       ch=ch+1
    elif i.isnumeric():
         n=n+1
print("total character :",ch)
print("total numeric :",n)
