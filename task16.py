person = {"name": "Ali", "age": 25, "city": "Tashkent"}

kalit = input("Kalit nomi: ")

if kalit in person:
    person.pop(kalit)
    print(person)
else:
    print("Bunday kalit yo'q")