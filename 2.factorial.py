# Write a python program to get the Factorial number of given number.
# 5*4*3*2*1=120


num=int(input("Enter number:"))
fact=1
for i in range (1,num+1):
    fact=fact*i
print("Factorial number is:",fact)


