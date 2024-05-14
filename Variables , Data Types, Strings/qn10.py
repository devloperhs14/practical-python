"""
Determine if given no plate could belong to the criminal or not. Print True if the number plate 
contains TN07 and False otherwise. Assume no plate of format: AA00AA00
"""
#input
no_plate = input()

#print
#print("TN07" in no_plate) # False, True

# print using slicing
print(no_plate[:4]=="TN07" or no_plate[4:]=="TN07")


