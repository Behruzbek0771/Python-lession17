def group_students(students: list[dict[str, str]]) -> dict[str, list[str]]:
    groups = {}

    for student in students:
        groups.setdefault(student['group'], []).append(student['name'])
    return groups

students = [
    {
        "name" : "Ali",
        "group" : "A"
    },
    {
        "name" : "Soli",
        "group" : "A"
    },
    {
        "name" : "Vali",
        "group" : "B"
    },
    {
        "name" : "Karim",
        "group" : "B"
    }
]
result = group_students(students)
print(result)