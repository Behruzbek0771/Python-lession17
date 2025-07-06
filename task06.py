users = {
    'first name':'Behruzbek',
    'last name':'Qalandarov',
    'age' : 20
}

key = input("key nommi: ")

if key in users:
    print(users[key])
else:
    print("Topilmadi")