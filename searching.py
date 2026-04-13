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
    # get current working directory path
    cwd_path = Path.cwd()

    file_path = cwd_path / file_name


    allowed_fields = {'unordered_numbers', 'ordered_numbers', 'dna_sequence'}
    if field not in allowed_fields:
        return None

    with open(file_path, mode='r', encoding='utf-8') as file:
        data = json.load(file)

        return data.get(field)




def main():
    sequential_data = read_data('sequential.json', 'unordered_numbers')

    print("Načtená data (unordered_numbers):")
    print(sequential_data)


if __name__ == "__main__":
    main()