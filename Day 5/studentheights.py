student_heights = input("Input a list of student heights ").split()
a = 0
heights = 0
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
    heights += student_heights[n]
    a += 1
#could also do | for height in student_heights      |
#              |     heights += studentheights[n]   |

final = round(heights / a)
print(max(student_heights)) #gets highest in list
print(min(student_heights)) #gets lowest in list
print(final)