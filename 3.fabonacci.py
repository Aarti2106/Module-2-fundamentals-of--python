#Write a pythone program to get the Fibonacci series of given range.
# 0 1 1 2 3 5 8 13 21 34 55 89

n=int(input("Enetr a number :"))
a,b=0,1
while b<n:
    print(b,end=" ")
    a,b=b,a+b
