from pathlib import Path
import json
import time
import random
import matplotlib.pyplot as plt


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


def pattern_search(sequence, pattern):
    positions = set()
    for i in range(len(sequence) - len(pattern) + 1):
        for j in range(len(pattern)):
            if sequence[i + j] != pattern[j]:
                break
        else:
            positions.add(i)
    return positions


def generate_sequence(size):
    return sorted([random.randint(1, size * 5) for _ in range(size)])


def measure_search_time(func, data, target, repeats=50):
    total_time = 0.0
    for _ in range(repeats):
        start_t = time.perf_counter()
        func(data, target)
        end_t = time.perf_counter()
        total_time += (end_t - start_t)
    return total_time / repeats


def measure_set_time(data_set, target, repeats=50):
    total_time = 0.0
    for _ in range(repeats):
        start_t = time.perf_counter()
        _ = target in data_set
        end_t = time.perf_counter()
        total_time += (end_t - start_t)
    return total_time / repeats


def run_experiments_and_plot():
    sizes = [100, 500, 1000, 5000, 10000, 20000]

    linear_times = []
    binary_times = []
    set_times = []

    for size in sizes:
        seq = generate_sequence(size)
        target = seq[-1]
        data_set = set(seq)

        avg_linear = measure_search_time(linear_search, seq, target)
        avg_binary = measure_search_time(binary_search, seq, target)
        avg_set = measure_set_time(data_set, target)

        linear_times.append(avg_linear)
        binary_times.append(avg_binary)
        set_times.append(avg_set)

    plt.figure(figsize=(10, 6))
    plt.plot(sizes, linear_times, label='Sekvenční vyhledávání (List)', marker='o', color='blue')
    plt.plot(sizes, binary_times, label='Binární vyhledávání (List)', marker='s', color='orange')
    plt.plot(sizes, set_times, label='Hledání v množině (Set)', marker='^', color='green')

    plt.xlabel('Počet prvků v sekvenci')
    plt.ylabel('Průměrný čas běhu (sekundy)')
    plt.title('Závislost času běhu vyhledávacích algoritmů na velikosti vstupu')
    plt.legend()
    plt.grid(True)
    plt.show()

    print("\n--- Zhodnocení asymptotické složitosti ---")
    print("Z grafu je patrné, že sekvenční vyhledávání roste lineárně O(n) s počtem prvků.")
    print("Binární vyhledávání je extrémně rychlé i pro velké vstupy, odpovídá logaritmické složitosti O(log n).")
    print(
        "Vyhledávání v množině (set) je nejrychlejší s konstantní složitostí O(1), křivka je zcela plochá nezávisle na velikosti dat.")


def main():
    target_number = 78

    sequential_data = read_data('sequential.json', 'unordered_numbers')

    print("Načtená data (unordered_numbers):")
    print(sequential_data)

    start_linear = time.perf_counter()
    result_linear = linear_search(sequential_data, target_number)
    end_linear = time.perf_counter()

    print(f"Výsledek vyhledávání čísla {target_number}:")
    print(result_linear)
    print(f"Čas sekvenčního vyhledávání: {end_linear - start_linear} sekund")

    ordered_numbers = read_data('sequential.json', 'ordered_numbers')

    print("\nNačtená data (ordered_numbers):")
    print(ordered_numbers)

    start_binary = time.perf_counter()
    result_binary = binary_search(ordered_numbers, target_number)
    end_binary = time.perf_counter()

    print(f"Výsledek binárního vyhledávání čísla {target_number}:")
    print(result_binary)
    print(f"Čas binárního vyhledávání: {end_binary - start_binary} sekund")

    print("\nSpouštím výkonnostní testy a generování grafu...")
    run_experiments_and_plot()

    target_pattern = 'ATA'
    dna_sequence = read_data('sequential.json', 'dna_sequence')

    print("\nNačtená data (dna_sequence):")
    print(dna_sequence)

    result_pattern = pattern_search(dna_sequence, target_pattern)
    print(f"Výsledek vyhledávání vzoru '{target_pattern}':")
    print(result_pattern)


if __name__ == "__main__":
    main()