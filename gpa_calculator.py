# my first python portfolip script
print("welcome to my grade tracker")

#1. store your current grades in variables
subject_1 = "comsci theory"
grade_1 = 95.9

subject_2 = "data structures"
grade_2 = 88.5

subject_3 = "algorithm"
grade_3 = 88.2

#calculate the average using simple math logic
total_score = grade_1 + grade_2 + grade_3 
average_grade = total_score / 3

# output the results to the screen
print(f"subject 1: {subject_1} | Grade: {grade_1}")
print(f"subject 2: {subject_2} | Grade: {grade_2}")
print(f"subject 3: {subject_3} | Grade: {grade_3}")
print("------------------------------")
print(f"your calculated average grade is: {average_grade}")

# conditional check to see if you passed
if average_grade >= 75.0:
    print("status: passsed!")
else:
    print("status: failed")