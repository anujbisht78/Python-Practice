""" Write a program that will give you the sum of even digits and  product of odd digits of a number"""

num=int(input("Enter the Number: "))
sum=0
prod=1
while num>0:
    digit=num%10
    if digit%2==0:
        sum=sum+digit
    else:
        prod=prod*digit
    num=num//10
    
print("Sum of Even Digits: ",sum)
print("Product of Odd Digits: ",prod)

    
