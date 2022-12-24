#Write a python program to sum of the first n positive integer.

sum=0
a=1

n=int(input("Enter a number :"))
for i in range(1,n+1):
      sum=sum+a
      a=a+1
print("sum of the n number is :",sum)
