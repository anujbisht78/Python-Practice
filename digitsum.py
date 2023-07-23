""" Write a program that will give you the sum of digits"""

num=int(input("Enter the Number: "))
sum=0
while num>0:
    
    digit=num%10
    sum=sum+digit
    num=num//10    

print("Sum is ",sum)
    



    

