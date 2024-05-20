# Accept a positive integer x as input, compute the value of this continued fraction and store 
# the result in a variable named cfrac and print the result 

# x -> input -> continued fraction -> cfrac -> print

# user input
x = int(input())

#setup
x1 = x + (1/x)
x2 = x + (1/x1)
x3 = x + (1/x2)
x4 = x + (1/x3)
x5 = x + (1/x4)
cfrac = x + (1/x5)

print(round(cfrac,2))