"""User will input (2numbers).Write a program to swap the numbers"""

num1=int(input("Enter the 1st number: "))
num2=int(input("Enter the 2nd number: "))
print("Before Swaping: ")
print("num1 = ",num1)
print("num2 = ",num2)

temp=num2
num2=num1
num1=temp
print("After Swapping: ")
print("num1 = ",num1)
print("num2 = ",num2)
