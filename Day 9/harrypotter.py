student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}
grades = ""

for student in student_scores:
    if student_scores[student] > 90:
        grades = "Outstanding"
    elif student_scores[student] > 80 and student_scores[student] <= 90: 
        grades = "Exceeds Expectations"
    elif student_scores[student] > 70 and student_scores[student] <= 80:
        grades = "Acceptable"
    else:
        grades = "Fail"
    student_grades[student] = grades

print(student_grades)