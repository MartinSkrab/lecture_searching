from pathlib import Path
import json


def read_data(file_name, field):
    cwd_path = Path.cwd()
    file_path = cwd_path / file_name

    allowed_fields = {'unordered_numbers', 'ordered_numbers', 'dna_sequence'}
    if field not in allowed_fields:
        return None

    with open(file_path, mode='r', encoding='utf-8') as file:
        data = json.load(file)
        return data.get(field)


def linear_search(sequence, target):
    positions = []
    count = 0

    for i in range(len(sequence)):
        if sequence[i] == target:
            positions.append(i)
            count += 1

    return {'positions': positions, 'count': count}


def binary_search(sequence, target):
    left = 0
    right = len(sequence) - 1

    while left <= right:
        mid = (left + right) // 2

        if sequence[mid] == target:
            return mid
        elif sequence[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return None


def main():
    sequential_data = read_data('sequential.json', 'unordered_numbers')
    print("Načtená data (unordered_numbers):")
    print(sequential_data)

    target_number = 5
    result = linear_search(sequential_data, target_number)
    print(f"Výsledek vyhledávání čísla {target_number}:")
    print(result)

    ordered_data = read_data('sequential.json', 'ordered_numbers')
    print("\nNačtená data (ordered_numbers):")
    print(ordered_data)

    binary_result = binary_search(ordered_data, target_number)
    print(f"Výsledek binárního vyhledávání čísla {target_number}:")
    print(binary_result)


if __name__ == "__main__":
    main()