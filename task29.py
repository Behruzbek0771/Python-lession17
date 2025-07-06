def get_active_users(users: dict[str, dict[str, bool | str]]) -> list[str]:
    aktive = []
    for user in users:
        if users[user] == True:
             aktive.append(user)
    return aktive

users = {
    "Ali" : False,

    "Vali" : False,

    "Ozod" : True,

    "Quvonch" : True,

    "Islom" : True,

    "Anvar" : True,

}
result = get_active_users(users)
print(result)