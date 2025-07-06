def group_by_length(words: list[str]) -> dict[int, list[str]]:
    new_dict = {}
    for i in words:
        text = len(i)
        new_dict.setdefault(text,[]).append(i)
    return new_dict
words =[
    "Salom",
    "python",
    "pythonini o'rganish oson",
    "hazillashdam osonmas",
    "lekin oson ish yo'q",
    "demak o'rganman"
]
result = group_by_length(words)
print(result)