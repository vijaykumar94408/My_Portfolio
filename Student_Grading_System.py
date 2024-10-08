# lists of subjects
subjects = ['Maths', 'Science', 'English']
#entered input subject scores are stored in this empty list 
scores = []
# iterating subjects inputs in empty list 
for subject in subjects:
    while True:
        #using try and catch method to handle exceptions
        try:
            # taking  inputs from user
            score = float(input("Enter score for  (0-100): "))
            #checking whether input is valid or not 
            if 0 <= score <= 100:
                #after every inputs from user, inputs are stroing into empty list
                scores.append(score)
                break #here breaking while loop to not repeat
            else:
                print("Please enter a value between 0 and 100.")
        except Exception as e:
            print("Invalid input, please enter a numeric value.")

total = sum(scores)  # calculating total sum of scores  
average = total / len(subjects) #doing average and 
# then comparing the average score according to the grade and feedback and then printing final output
if 90 <= average <= 100:
    grade = 'A'
    feedback = "Excellent"
elif 80 <= average < 90:
    grade = 'B'
    feedback = "Good"
elif 70 <= average < 80:
    grade = 'C'
    feedback = "Better"
elif 60 <= average < 70:
    grade = 'D'
    feedback = "Not Bad"
else:
    grade = 'F'
    feedback = "Try Harder"

print(f"\nAverage Score:",average)
print("Grade",grade)
print("Feedback:",feedback)
