import pandas
import random

names_list = {"student": ["Beth", "Caroline", "James"],
              "score": [23, 76, 89]
              }
student_data_frame = pandas.DataFrame(names_list)
# print(student_data_frame)

# for (key, value) in student_data_frame.items():
#     print(value)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    print(row.student)
