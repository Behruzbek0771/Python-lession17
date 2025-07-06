def group_indices(numbers: list[int]) -> dict[int, list[int]]:
    result = {}

    for index, number in enumerate(numbers):
        result.setdefault(number, []).append(index)

    return result

numbers = [1, 2, 1, 3, 2, 1]
print(group_indices(numbers))
