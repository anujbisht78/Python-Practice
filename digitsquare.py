""" Write a Program to find the sum of Sqaure of digits of a number"""

num=int(input("Enter the Number: "))
sqr=int
sum=0
while num>0:
    digit=num%10
    sqr=digit*digit
    sum=sum+sqr
    num=num//10

print("Square of digits: ",sum)
