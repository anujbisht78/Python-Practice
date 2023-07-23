""" Write a program that will give you the product of digits"""

num=int(input("Enter the Number: "))
prod=1
while num>0:
    digit=num%10
    prod=prod*digit
    num=num//10
    
print("Produt is : ",prod)
