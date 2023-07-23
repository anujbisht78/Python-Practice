"""Write a Program of finding the sum of cube of digits of the numbers """

num=int(input("Enter the Number: "))
sum=0
cube=int
while num>0:
    digit=num%10
    cube=digit*digit*digit
    sum=sum+cube
    num=num//10
print("Cube of digits oa the number: ",sum)
