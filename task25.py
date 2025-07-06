def group_by_age(people: list[dict[str, int | str]]) -> dict[int, list[str]]:
    royhat = {}

    for i in people:
        royhat.setdefault(i["age"], []).append(i["name"])
        
    return royhat

people =[
    {
        "name" : "Ali",
        "age" : 19
    },
    {
        "name" : "Vali",
        "age" : 22
    },
    {
        "name" : "Ozod",
        "age" : 19
    },
    {
        "name" : "Quvonch",
        "age" : 20
    },
    {
        "name" : "Islom",
        "age" : 19
    },
    {
        "name" : "Anvar",
        "age" : 22
    }
]
result = group_by_age(people)
print(result)