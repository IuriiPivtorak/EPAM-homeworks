students_count = int(input('input number of students: '))
tasks_count = int(input('input number of tasks: '))

students_names = [] # list for the names
for i in range(students_count):
    student_name = input('input name of the student: ')
    students_names.append(student_name)

tasks_marks = [] # list of lists for marks
for student in students_names:
    task_marks = []
    for task in range(tasks_count):
        task_mark = int(input('input mark for task {} for {}: '.format(task+1, student)))    
        while task_mark <0 or task_mark > 10:
            print('You must enter values from 0 to 10')
            task_mark = int(input('input mark for task {} for {}: '.format(task+1, student)))
        task_marks.append(task_mark)
    tasks_marks.append(task_marks)

ratings = [] # list for sum of marks for each student
for i in tasks_marks:
    rating = sum(i)
    ratings.append(rating)

merged = zip(students_names, ratings)
merge = list(merged) # list of names and marks
try:
    print('Top 1: {} with score of {}'.format(sorted(merge, key=lambda x: int(x[1]))[-1][0],
                                              sorted(merge, key=lambda x: int(x[1]))[-1][1]))
except IndexError:
    pass
try:
    print('Top 2: {} with score of {}'.format(sorted(merge, key=lambda x: int(x[1]))[-2][0],
                                              sorted(merge, key=lambda x: int(x[1]))[-2][1]))
except IndexError:
    pass
try:
    print('Top 3: {} with score of {}'.format(sorted(merge, key=lambda x: int(x[1]))[-3][0],
                                              sorted(merge, key=lambda x: int(x[1]))[-3][1]))
except IndexError:
    pass

sum_of_marks = [sum(i) for i in zip(*tasks_marks)] # list of sum of marks for each task
task_numbers = [] # list of task numbers
for i in range(len(sum_of_marks)):
    number = str(i + 1)
    task_numbers.append(number)
total = zip(task_numbers, sum_of_marks)
total = list(total) # list of lists of sum of marks and task numbers

try:
    print('1st hardest task: number {} with total score of {}'.format(sorted(total, key=lambda x: int(x[1]))[0][0],
                                                                      sorted(total, key=lambda x: int(x[1]))[0][1]))
except IndexError:
    pass
try:
    print('2nd hardest task: number {} with total score of {}'.format(sorted(total, key=lambda x: int(x[1]))[1][0],
                                                                      sorted(total, key=lambda x: int(x[1]))[1][1]))
except IndexError:
    pass
try:
    print('3rd hardest task: number {} with total score of {}'.format(sorted(total, key=lambda x: int(x[1]))[2][0],
                                                                      sorted(total, key=lambda x: int(x[1]))[2][1]))
except IndexError:
    pass
