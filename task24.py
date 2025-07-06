def most_common_char(text: str) -> str:
    freq = {}

    for char in text:
        freq[char] = freq.get(char, 0) + 1

    return max(freq, key=lambda x: freq[x])

text = "shhfweehviwhoafsdgzddgggggggggggghfgacsdv"

result = most_common_char(text)
print(result)