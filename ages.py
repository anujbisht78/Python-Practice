"""User will input (3ages).Find the oldest and youngest  one"""

# a=int(input("Enter the one age: "))
# b=int(input("Enter the 2nd age: "))
# c=int(input("Enter the 3rd age: "))
# print("oldest one is: ",max(a,b,c))
# print("youngest one is: ",min(a,b,c))

#without in built function
a=int(input("Enter the one age: "))
b=int(input("Enter the 2nd age: "))
c=int(input("Enter the 3rd age: "))  

if a>b and a>c:
    print("oldest one: ",a)
elif b>a and b>c:
    print("oldest one: ",b)
else:
    print("oldest one: ",c)
    
    
