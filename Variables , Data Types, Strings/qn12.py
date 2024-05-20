'''
You are given a string and two non-negative integers as input. # string, # + integers 
The two integers specify the start and end indices of a substring in the given string.  
 
Create a new string by replicating the substring a minimum number of times so that the 
resulting string is longer than the input string. 

The input parameters each on new line are:
the string, 
start index of the substring and 
the end index of substring (endpoints inclusive) 
'''

# user_input
string = input()
start = int(input())
end = int(input())

# substring
substring = string[start:end+1]

# repetations
min_rep = len(string)//len(substring)+1

# new_string
new_string = substring*min_rep
print(new_string)




