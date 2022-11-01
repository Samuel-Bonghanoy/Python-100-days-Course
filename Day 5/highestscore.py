student_scores = input("Input a list of student scores ").split()
maximum = int(0)
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
    if student_scores[n] > maximum:
        maximum = student_scores[n]
print(student_scores)
print(f"The highest score in the class is: {maximum}")

for score in student_scores:
    if score > maximum:
        maximum = score
print(f"The highest score in the class is: {maximum}")