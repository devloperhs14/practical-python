"""
Print the following pattern. There is exactly one space between any two consecutive numbers 
on any line. There are no spaces at the end of any line. 
1 2 1 
1 2 3 2 1 
1 2 3 4 3 2 1 
1 2 3 4 5 4 3 2 1
"""

# nested for loop and range
rows = 6

for i in range(1, rows+1): 
    # print no from 1 to i
    for j in range(1,i+1):
        print(j, end = " ")
    
    # print no from i-1 down to 1
    for j in range(i-1,0,-1):
        print(j , end =" ")
    print()



