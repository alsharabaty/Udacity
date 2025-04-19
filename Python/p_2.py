# 1. Create a list of student names
def get_student_names():
    names = []
    while True:
        name = input("Enter a student name (or 'done' to finish): ")
        if name.lower() == 'done':
            break
        names.append(name)
    return names

# 2. Create a list of assignments left to submit
def assigments():
    assignments = []
    while True:
        assignment = input("Enter the number of assignments left to submit (or 'done' to finish): ")
        if assignment.lower() == 'done':
            break
        try:
            assignments.append(int(assignment))
        except ValueError:
            print("Please enter a valid number.")
    return assignments

# 3. Create a list of grades
def grades():
    grades = []
    while True:
        grade = input("Enter the current grade (or 'done' to finish): ")
        if grade.lower() == 'done':
            break
        try:
            grades.append(float(grade))
        except ValueError:
            print("Please enter a valid number.")
    return grades

# 4. Create a list of maximum grades
def max_grades():
    max_grades = []
    while True:
        max_grade = input("Enter the maximum grade (or 'done' to finish): ")
        if max_grade.lower() == 'done':
            break
        try:
            max_grades.append(float(max_grade))
        except ValueError:
            print("Please enter a valid number.")
    return max_grades

assigments = assigments()
names = get_student_names()
grades = grades()
max_grades = max_grades()


## message string to be used for each student
## HINT: use .format() with this string in your for loop

for i in range(len(names)):
    name = names[i]
    assignment = assigments[i]
    grade = grades[i]
    max_grade = max_grades[i]
    message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
    submit before you can graduate. Your current grade is {} and can increase \
    to {} if you submit all assignments before the due date.\n\n".format(name, assignment, grade, max_grade)
    print(message)

## write a for loop that iterates through each set of names, assignments, and grades to print each student's message