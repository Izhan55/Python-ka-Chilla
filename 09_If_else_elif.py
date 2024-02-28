arham_age=5
required_age_at_school=5

#question: can arham go to school
if arham_age==required_age_at_school:
    print("Congratulation! Arham can go to school")
elif arham_age > required_age_at_school:
    print("Arham should join higher secondary school")
elif arham_age <= 2:
    print("you should take care of arham, he is still a baby! ")
else:
    print("Arham can not go to school")

#Input function for Results: 


required_pak_number_for_Recommendation= 528007
pak_number=input("Enter your pak number ")

if required_pak_number_for_Recommendation == 528007:
    print("Congratulation! You got recommended from ISSB")
else:
    print("Sorry! I regret to tell you this you got Not Recommended!")