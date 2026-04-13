from pathlib import Path
import json


def read_data(file_name, field):
    """
    Reads a JSON file and returns data for a given field.

    Args:
        file_name (str): Name of the JSON file.
        field (str): Key to retrieve from the JSON data.
            Must be one of: 'unordered_numbers', 'ordered_numbers' or 'dna_sequence'.

    Returns:
        list | str | None:
            - list: If data retrieved by the selected field contains numeric data.
            - str: If field is 'dna_sequence'.
            - None: If the field is not supported.
    """
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


def main():
    sequential_data = read_data('sequential.json', 'unordered_numbers')

    print("Načtená data (unordered_numbers):")
    print(sequential_data)

    target_number = 5
    result = linear_search(sequential_data, target_number)

    print(f"Výsledek vyhledávání čísla {target_number}:")
    print(result)


if __name__ == "__main__":
    main()