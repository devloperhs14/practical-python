# 2D Quadrant Checker
'''
Accept a point in 2D space as input and find the region in space that this point belongs to. 
A point could belong to one of the four quadrants (I, II , III, IV), 
or it could be on one of the two axes, 
or it could be the origin. 

Rules:
Input: x, y (seprate lines)
Output: first, second, third, fourth, x-axis, y-axis, and origin
'''

# user input
x = float(input())
y = float(input())

if x==0 and y==0:
    print("origin")
elif y == 0 and x!=0:
    print("x-axis")
elif y!=0 and x==0:
    print("y-axis")
elif x>0 and y>0:
    print("first")
elif x<0 and y>0:
    print("second")
elif x<0 and y<0:
    print("third")
elif x>0 and y<0:
    print("fourth")
