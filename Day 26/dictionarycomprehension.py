import random

names_list = ["Alex", "Beth", "Caroline", "Dave", "Elearnor", "Freddie"]

students_scores = {student:random.randint(1, 100) for student in names_list}
print(students_scores)


passed_students = {student:grade for (student, grade) in students_scores.items() if grade > 60}
print(passed_students)

# looping through dictionaries
for (key, value) in students_scores.items():
    print(value)