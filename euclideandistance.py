"""Write a program to find the euclidean distance between two coordinates"""

import math

x1=float(input("Enter the x1 for x coordinate: "))
x2=float(input("Enter the x2 for x coordinate: "))
y1=float(input("Enter the y1 for y coordinate: "))
y2=float(input("Enter the y2 for y coordinate: "))

d=math.sqrt(((x2-x1)**2)+((y2-y1)**2))
print("Distance between two point is ",float(d))