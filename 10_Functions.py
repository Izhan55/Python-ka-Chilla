
# defining a function

# 1
def print_codanics():
    print("we are learning python with Ammar")
    print("we are learning python with Ammar")
    print("we are learning python with Ammar")

print_codanics()

# # 2
def print_codanics():
    text = "we are learning python with Ammar in codanics youtube channel"
    print(text)
    print(text)
    print(text)

print_codanics()

 # 3

def print_codanics(text):
    print(text)
    print(text)
    print(text)

print_codanics("we are learning python with ammar in codanics youtube channel")


# # defining a function with if,elif and else statement

def schoool_calculator(age):
    if age==5:
        print("hammad can join the school")
    elif age>5:
        print("hammad should join higher school")
    else:
        print("hammad is still a baby")

schoool_calculator(15)

# defining a function of future

def future_age(age):
    new_age=age+20
    return new_age
    print(new_age)

future_predicted_age= future_age(22)
print(future_predicted_age)