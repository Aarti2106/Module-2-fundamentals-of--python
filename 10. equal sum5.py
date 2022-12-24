#Write a python program that will return true if the two given integer value are equal or
#their sum or difference is 5.

a=int(input("Enter number A:"))
b=int(input("Enter number B:"))

if a==b:
    print("return True")
elif a+b==5:
    print("return True")
elif a-b==5:
    print("return True")
else:
    print("False")
