def count_names(names: list[str]) -> dict[str, int]:
    new_dict = {}

    for name in names:
        new_dict.setdefault(name,names.count(name))
    
    return new_dict

names = ["Ali",  "Ali",  "Ali", "Vali", "Vali","Sami"]

print(count_names(names))