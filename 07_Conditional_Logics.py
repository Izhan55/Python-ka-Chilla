    
# logical operators are either "True or False" or "yes or no" or "0 or 1"
    # equal to                         ==
    # not equal to                     !=
    # less than                        <
    # greater than                     >
    # less than and equal to           <=
    # greater than equal to            >=   
    # AND operator                      &
    # OR operator                       |   (also called bitwise-OR)
    # NOT operator 
    # True
    # False                     ~
    # bitwise shift left                << 
    # bitwise shift right               >>
    

print(4==4)
print(4!=4)
print(4>3)
print(3>6)
print(3<=5)
print(5>=4)

# appliaction of logical operators

arham_age=4
age_at_school=5
print(arham_age==age_at_school)

# input function and logical operator

age_at_school=5
arham_age=input("how old is arham? ")     #input function
arham_age=int(arham_age)
print(type(arham_age))
print(arham_age==age_at_school)             #logical operator
