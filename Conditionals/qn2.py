"""
Accept the value of x as input and print the value of f(x) as output. 
f(x) is a piece wise fn (qn2.png)

Condtions: 
* both the input x and output f(x) should be real numbers / float
"""

#user input
x = float(input())

if 0<x<10:
    print(x+2)
elif 10<=x:
    print((x**2)+2)
else:
    print(0)
