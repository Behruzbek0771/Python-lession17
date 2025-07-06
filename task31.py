def count_letters(text: str) -> dict[str, int]:
    result = {}
    for char in text:
        if char.isalpha():
            result[char] = result.get(char, 0) + 1
    return result

text = "assalomu alaykum"
print(count_letters(text))
