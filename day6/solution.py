import math

puzzle_input: str = "day6/input.txt"


def read_input(input_data: str) -> list[str]:
    if isinstance(input_data, str) and '\n' in input_data:
        lines = input_data.strip().split('\n')
    else:
        with open(input_data, "r") as file:
            lines = file.read().splitlines()
    return lines


def parse_ops_line(ops_line: str) -> tuple[list[str], list[int]]:
    ops = []
    starts = []
    for i, char in enumerate(ops_line):
        if char in '+*':
            ops.append(char)
            starts.append(i)
    starts.append(None)
    return ops, starts


def cols_to_numbers(digit_cols: list[tuple]) -> list[int]:
    numbers = []
    for col in digit_cols:
        joined = ''.join(char for char in col if char != ' ')
        if joined:  # skip empty
            numbers.append(int(joined))
    return numbers


def apply_op(numbers: list[int], op: str) -> int:
    return sum(numbers) if op == '+' else math.prod(numbers)


def solve_part1(input: str) -> int:
    lines = read_input(input)
    ops = lines.pop().split()
    rows = [list(map(int, line.split())) for line in lines]
    result = sum( 
        apply_op(col, op)
        for col, op in zip(zip(*rows), ops)
    )
    return result


def solve_part2(input: str) -> int:
    lines = read_input(input)
    total_result = 0
    
    ops_line = lines.pop()
    ops, starts = (parse_ops_line(ops_line))
    for i, op in enumerate(ops):
        group_slices = [line[starts[i]:starts[i+1]] for line in lines]
        digit_cols = list(zip(*group_slices))
        numbers = cols_to_numbers(digit_cols)
        total_result += apply_op(numbers, op)
    
    return total_result


if __name__ == "__main__":
    solution1 = solve_part1(puzzle_input)
    solution2 = solve_part2(puzzle_input)
    print(f"\n\nsolution part 1 : {solution1}")
    print(f"\nsolution part 2 : {solution2}")