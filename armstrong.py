"""Write aProgram to check wheather a given number is armstrong or not"""
#Armstrong Number: whose sum of the cube of digits is equal to the number itself



num=int(input("Enter the Number: "))
sum=0
copy_num=num
cube=int
while num>0:
    digit=num%10
    cube=digit*digit*digit
    sum=sum+cube
    num=num//10
    
if(sum==copy_num):
    print(copy_num,"is an Armstrong")
else:
    print(copy_num,"is not a Armstrong")
