#Write a Python program to count the occurrences of each word in a given
#sentence.

str=input("Enter string :")
str=str.split()
print(str)

i=0
while i<len(str):
    count=0
    for j in str:
        if str[i]==j:
            count=count+1
    print(str[i],"present",count,"times")

    i=i+1
