puzzle_input: str = "day10/input.txt"


def read_input(input_data: str) -> list[str]:
    if isinstance(input_data, str) and '\n' in input_data:
        lines = input_data.strip().split('\n')
    else:
        with open(input_data, "r") as file:
            lines = file.read().splitlines()
    return lines

def solve_part1(input: str) -> int:
    return 1

def solve_part2(input: str) -> int:
    return 1


if __name__ == "__main__":
    solution1 = solve_part1(puzzle_input)
    solution2 = solve_part2(puzzle_input)
    print(f"\n\nsolution part 1 : {solution1}")
    print(f"\nsolution part 2 : {solution2}")