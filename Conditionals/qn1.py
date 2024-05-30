# Accept a non-zero integer as input. Print positive if it is greater than zero and negative if it is less than zero.

x = int(input())

if x>0:
    print("positive")
elif x<0:
    print("negative")
else:
    print("invalid")