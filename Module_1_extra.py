grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
list = [
    {'name': 'Johnny', 'grades': [5, 3, 3, 5, 4]},
    {'name': 'Bilbo', 'grades': [2, 2, 2, 3]},
    {'name': 'Steve', 'grades': [4, 5, 5, 2]},
    {'name': 'Khendrik', 'grades': [4, 4, 3]},
    {'name':'Aaron', 'grades': [5, 5, 5, 4, 5]}
]
for student in list:
    average_mark = sum(student['grades']) / len(student['grades'])
    student['average mark'] = average_mark

for student in list:
    print(f"{student['name']}: {student['average mark']}")