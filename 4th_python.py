import random

total_students = 40
total_teams = 10

students = range(total_students)

list_students = list(students)

random.shuffle(list_students)

project_team = []

for i in range(total_teams):
    num_of_members = int(total_students/total_teams)
    index = i * num_of_members
    project_team.append(list_students[index:index+num_of_members])

for i in project_team:
    print(i)