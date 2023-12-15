# CTI-110
# P4HW1 - Score List
# Nick Osterkamp
# 11/22/2023

num_scores = int(input("How many scores do you want to enter? "))

scores = []

for i in range(1, num_scores + 1):
    while True:
        try:
            score = float(input(f"Enter score #{i}: "))
            
            if 0 <= score <= 100:
                scores.append(score)
                break
            else:
                print("INVALID Score Entered!!!!")
                print("Score should be between 0 and 100")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

lowest_score = min(scores)
scores.remove(lowest_score)
average_score = sum(scores) / len(scores)

print("\n------------Results------------")
print(f"Lowest score : {lowest_score}")
print(f"Modified List : {scores}")
print(f"Scores Average : {average_score:.2f}")
if average_score >= 90:
    grade = 'A'
elif average_score >= 80:
    grade = 'B'
elif average_score >= 70:
    grade = 'C'
elif average_score >= 60:
    grade = 'D'
else:
    grade = 'F'
print(f"Grade : {grade}")
print("---------------------------------")

#1. Get the number of scores from the user.
#2. Create an empty list for scores.
#3. Collect scores from the user
#4  Make sure the scores are between 0 and 100.
#5. Calculate and store the lowest score.
#6. Remove the lowest score from the list.
#7. Calculate the average of the remaining scores.
#8. Display the lowest score, modified list, average, and letter grade.