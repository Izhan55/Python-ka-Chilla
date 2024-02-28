x=8            #integer
y=5.2          #float
z="Hello!"     #string  

#inplicit type conversion
x=x*y
print(x, "type of x is:", type(x))


# #explicit type of conversion  (Integer)
age=input("what is your age? ")
age=int(age)
print(age, type(int(age)))


#explicit type of conversion    (float)
age=input("what is your age? ")
# age=float(age)
print(age, type(float(age)))


#name
name=input("what is your name? ")
print(name, type(str(name)))