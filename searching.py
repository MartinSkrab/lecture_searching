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
    positions = [index for index, value in enumerate(sequence) if value == target]
    count = len(positions)

    return {'positions': positions, 'count': count}


def binary_search(sequence, target):
    start = 0
    end = len(sequence) - 1

    while start <= end:
        mid = start + (end - start) // 2

        if sequence[mid] == target:
            return mid
        elif sequence[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return None


def main():
    target_number = 5

    sequential_data = read_data('sequential.json', 'unordered_numbers')

    print("Načtená data (unordered_numbers):")
    print(sequential_data)

    result_linear = linear_search(sequential_data, target_number)

    print(f"Výsledek vyhledávání čísla {target_number}:")
    print(result_linear)

    ordered_numbers = read_data('sequential.json', 'ordered_numbers')

    print("\nNačtená data (ordered_numbers):")
    print(ordered_numbers)

    result_binary = binary_search(ordered_numbers, target_number)

    print(f"Výsledek binárního vyhledávání čísla {target_number}:")
    print(result_binary)


if __name__ == "__main__":
    main()