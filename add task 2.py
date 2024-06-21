#  File Reading:
# 1. Open the provided text file in read mode.
# 2. Read the contents of the file and store them in an
# appropriate data structure.

import random
import statistics

students = dict()

with open('students.txt', 'r') as file:
    content = file.readlines()

for line in content:
    line_2 = line.strip()
    name, score = line_2.split(' ')
    students[name] = [int(score)]
    students[name].extend([
        random.randint(0, 100),
        random.randint(0, 100),
        random.randint(0, 100),
        random.randint(0, 100),
    ])

with open('students_results.txt', 'w') as file:
    all_scores = []
    for student, scores in students.items():
        file.write(f'{student} {statistics.mean(scores)}\n')
        all_scores.extend(scores)

    file.write(f'min - {min(all_scores)}\n')
    file.write(f'max - {max(all_scores)}\n')
    file.write(f'class average - {statistics.mean(all_scores)}\n')
    file.write(f'mode - {statistics.mode(all_scores)}\n')
    file.write(f'median - {statistics.median(all_scores)}\n')
    file.write(f'variance - {statistics.variance(all_scores)}\n')


# 2. Data Processing:
# 1. Split each line of the file into student name and
# test score.
# 2. Calculate the average score for each student.


# 3. File Writing:
# 1. Open a new text file in write mode to store the
# results.
# 2. Write the student names along with their average