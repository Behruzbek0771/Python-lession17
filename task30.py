def filter_non_zero(d: dict[str, int]) -> dict[str, int]:
    new_dict = {}
    for key,values in d.items():
        if values != 0:
            new_dict[key] = values

    return new_dict

    # for i in d:
    #     if d[i] != 0: 
    #      new_dict[i] = d[i]
    # return new_dict

d = {
    "olma" : 13,
    "banan" : 0,
    "uzum" : 10,
    "anor" : 3,
    "olcha" : 0

}
result = filter_non_zero(d)
print(result)