
'''
Write a program to realize the equation of a line given 2 points (x1,y1) and (x2,y2) in 2D space.
Hint - see qn5.py to calculate.

Input (5 lines) 
x1,y1
x2,y2
x3

Output (2 lines) : 
if line vertical :
    y3 = vertical
if not:
    y3 = Positive , Negative , Zero
'''


# user_input
x1 , y1 = float(input()), float(input()) # 1st point
x2 , y2 = float(input()), float(input()) # 2nd point
x3 = float(input())
#y3?


# vertical line x1!=x2

if x1!=x2:
    #calc slope
    m = (y2-y1)/(x2-x1) 

    #y3 = m(x3-x1)+y1
    y3 = m*(x3-x1)+y1
    print(y3)

    # slope type
    if m ==0:
        print("Horizontal Line")
    elif m>0:
        print("Positive Slope")
    else:
        print("Negative Slope")

else:
    print("Vertical Line")



