#Question 3.

# Get the class score as input from user.
class_score = float(input("Please, Enter the class score: "))

# Checks the class score and assign the respective grade
if(class_score>=90 and class_score<=100):
    print("Grade A")
elif(class_score>=80 and class_score<90):
    print("Grade B")
elif(class_score>=70 and class_score<80):
    print("Grade C")
elif(class_score>=60 and class_score<70):
    print("Grade D")
elif(class_score>=0 and class_score<60):
    print("Grade F")
else:
    # Handles the case when class score given is invalid.
    print("Please enter a valid score")  
