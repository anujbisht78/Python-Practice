"""
Making an high order function 
we have a list and we have to find out the 
sum of even numbers
sum if odd numbers
sum of numbers divisible by 3
"""
def returnfun(fun,l):
    sum=0
    for i in l:
        if fun(i):
            sum=sum+i
    
    return sum

x= lambda x: x%2==0
y= lambda x: x%2!=0
z= lambda x: x%3==0


l=[1,54,10,23,14,22,20,13,16]

print("Sum of even Numbers",returnfun(x,l))
print("Sum of odd Numbers",returnfun(y,l))   
print("Sum of numbers divisible by 3",returnfun(z,l))  

