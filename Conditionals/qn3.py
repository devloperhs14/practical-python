'''
Accept an integer as input and print time of the day (qn3.png)

Rules
Input: single line containing an integer
Output: single line containing "Output" String
'''

# user_input
t = int(input())

if 0 <= t <= 5:
    print("NIGHT")
elif 6<= t <= 11:
    print("MORNING")
elif 12 <= t <= 17:
    print("AFTERNOON")
elif 18 <= t <= 23:
    print("EVENING")
else:
    print("INVALID")