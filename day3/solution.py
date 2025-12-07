puzzle_input: str = "day3/input.txt"


def read_input(input_data: str) -> list[str]:
    if isinstance(input_data, str) and '\n' in input_data:
        lines = input_data.strip().split('\n')
    else:
        with open(input_data, "r") as file:
            lines = [line.strip() for line in file.readlines()]
    return lines


def max_joltage(s: str, n: int) -> int:
    result = []
    start = 0
    for k in range(n):
        # Need (n - k - 1) more digits after this one
        end = len(s) - (n - k - 1)
        segment = s[start:end]
        max_char = max(segment)
        idx = segment.index(max_char)
        result.append(max_char)
        start = start + idx + 1
    return int(''.join(result))


def solve_part1(puzzle_input: str) -> int:
    battery = read_input(puzzle_input)
    total_joltage = 0

    for bank in battery:
        joltage = max_joltage(bank, 2)
        total_joltage += joltage
    
    return total_joltage


def solve_part2(input: str) -> int:
    battery = read_input(input)
    total_joltage = 0

    for bank in battery:
        joltage = max_joltage(bank, 12)
        total_joltage += joltage
    
    return total_joltage


if __name__ == "__main__":
    solution1 = solve_part1(puzzle_input)
    solution2 = solve_part2(puzzle_input)
    print(f"\n\nsolution part 1 : {solution1}")
    print(f"\nsolution part 2 : {solution2}")