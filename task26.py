def merge_dicts(a: dict, b: dict) -> dict:
    merged = {}
    for key in a:
        if key in b:
            merged[key] = b[key]
    return merged


a = {
    "name": "Ali",
    "age": 25,
    "grade": "A"
    }
b = {
    "name": "Vali",
    "age": 24,
    "email" : "vali@gmail.com"
    }
result = merge_dicts(a,b)
print(result)