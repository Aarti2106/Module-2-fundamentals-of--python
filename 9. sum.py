#Write a python program to sum of three given integers.however ,if two valuesare equal sum
#will be zero.

a=int(input("Enter  number A:"))
b=int(input("Enter  number B :"))
c=int(input("Enter  number C:"))

if a==b:
    print("a and b is eqaul to",0)
elif b==c:
    print("b and c is eqaul to",0)
elif a==c:
    print("a and c is eqaul to",0)

else:
    print("a and b and c sum is",a+b+c)

