"""Write a program to reverse a given number"""
    
num=int(input("Enter teh given number: "))
rev=0
while num>0:
    digit=num%10
    rev=rev+digit
    num=num//10
    
print("Reverse is: ",rev)

