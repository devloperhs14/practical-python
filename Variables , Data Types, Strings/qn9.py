"""
A simple algorithm has to be designed to find out whether a student belongs to the Data 
Science (DS) branch or not. The input will be a student's roll number, which is of the form 
BR18B0000. True/ False as output """

# roll no -> DS -> True; False - Specific Format BR18B0000
# if else condition 

#boolean
roll_no = input()

print(roll_no[:2]=="DS") # True , False

# one line code.