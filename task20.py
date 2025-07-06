permissions = {"read": True, "write": False, "delete": True}

for keys,value in permissions.items():
    if value == True:
        print(keys)