# CTI-110
# P2HW2 - List
# Nicholas Osterkamp
# 10/24/2023

grades = []

grades.append(float(input("Enter the grade for Module 1: ")))
grades.append(float(input("Enter the grade for Module 2: ")))
grades.append(float(input("Enter the grade for Module 3: ")))
grades.append(float(input("Enter the grade for Module 4: ")))
grades.append(float(input("Enter the grade for Module 5: ")))
grades.append(float(input("Enter the grade for Module 6: ")))

lowest_grade = min(grades)
highest_grade = max(grades)
sum_of_grades = sum(grades)
average_grade = sum_of_grades / len(grades)

print("------------Results------------")
print("Lowest grade: " + str(lowest_grade))
print("Highest Grade: " + str(highest_grade))
print("Sum of grades: " + str(sum_of_grades))
print("Average: " + str(format(average_grade, '.2f')))
print("-------------------------------")

# 1. Declare an empty list named 'grades'
# 2. Prompt the user to enter the grade for the current module
# 3. Append the entered grade to the 'grades' list
# 4. Find the lowest grade from the 'grades' list
# 5. Find the highest grade from the 'grades' list
# 6. Calculate the sum of all grades
# 7. Calculate the average of grades
# 8. Display the results