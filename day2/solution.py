puzzle_input: str = "day2/input.txt"


def read_input(input_data: str) -> list[str]:
    if isinstance(input_data, str) and '\n' in input_data:
        lines = input_data.strip().split('\n')
    else:
        with open(input_data, "r") as file:
            lines = file.readlines()
    return lines


def is_double_number(string_number: str) -> bool:
    if len(string_number) % 2 != 0:
        return False
    
    mid = len(string_number) // 2
    first_half = string_number[:mid]
    second_half = string_number[mid:]
    
    return first_half == second_half

def is_repeated_pattern(string_number: str) -> bool:
    length = len(string_number)

    for pattern_len in range(1, length // 2 + 1):
        if length % pattern_len == 0:
            pattern = string_number[:pattern_len]
            if pattern * (length // pattern_len) == string_number:
                return True
    return False

def check_range(ID_range: str, checker_func) -> int:
    start, stop = ID_range.split('-')
    total = 0
    for x in range(int(start), int(stop) + 1):
        if checker_func(str(x)):
            total += x
    return total


def solve_part1(puzzle_input: str) -> int:
    input = read_input(puzzle_input)
    IDs = input[0].split(',')
    total = 0
    for ID_range in IDs:
        total += check_range(ID_range, is_double_number)

    return total

def solve_part2(puzzle_input: str) -> int:
    input = read_input(puzzle_input)
    IDs = input[0].split(',')
    total = 0
    for ID_range in IDs:
        total += check_range(ID_range, is_repeated_pattern)

    return total


if __name__ == "__main__":
    solution1 = solve_part1(puzzle_input)
    solution2 = solve_part2(puzzle_input)
    print(f"\n\nsolution part 1 : {solution1}")
    print(f"\nsolution part 2 : {solution2}")