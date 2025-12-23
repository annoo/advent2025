from itertools import combinations
from functools import reduce
from scipy.optimize import milp, LinearConstraint, Bounds

puzzle_input: str = "day10/input.txt"


def read_input(input_data: str) -> list[str]:
    if isinstance(input_data, str) and '\n' in input_data:
        lines = input_data.strip().split('\n')
    else:
        with open(input_data, "r") as file:
            lines = file.read().splitlines()
    return lines


def parse_line(line: str) -> tuple[list[bool], list[tuple], list[int]]:
    _, rest = line.split('[', 1)
    lights_str, rest = rest.split(']', 1)
    
    indicator_lights = [c == '#' for c in lights_str]
    
    tuples_part, joltage_part = rest.split('{', 1)
    
    button_wirings = []
    for part in tuples_part.split('('):
        if ')' in part:
            content = part.split(')')[0]
            nums = tuple(int(x) for x in content.split(','))
            button_wirings.append(nums)
    
    joltage_str = joltage_part.split('}')[0]
    joltage_levels = [int(x) for x in joltage_str.split(',')]
    
    return indicator_lights, button_wirings, joltage_levels


# Part 1 helpers

def lights_to_bitmask(lights: list[bool]) -> int:
    mask = 0
    for i, on in enumerate(lights):
        if on:
            mask |= (1 << i)
    return mask


def wiring_to_bitmask(wiring: tuple) -> int:
    mask = 0
    for i in wiring:
        mask |= (1 << i)
    return mask


def create_button_masks(button_wirings: list[tuple]) -> set[int]:
    return {wiring_to_bitmask(button) for button in button_wirings}


def count_button_presses_for_lights(lights: int, buttons: set[int]) -> int:
    for num_presses in range(len(buttons) + 1):
        for combo in combinations(buttons, num_presses):
            result = reduce(lambda a, b: a ^ b, combo, 0)
            if result == lights:
                return num_presses


# Part 2 helpers

def build_button_matrix(button_wirings: list[tuple], num_counters: int) -> list[list[int]]:
    num_buttons = len(button_wirings)
    matrix = [[0] * num_buttons for _ in range(num_counters)]
    for button_idx, wiring in enumerate(button_wirings):
        for counter_idx in wiring:
            matrix[counter_idx][button_idx] = 1
    return matrix


def build_equations(button_wirings: list[tuple], joltage_levels: list[int]) -> tuple[list[list[int]], list[int]]:
    A = build_button_matrix(button_wirings, len(joltage_levels))
    return A, joltage_levels


def count_button_presses_for_joltage(button_wirings: list[tuple], joltage_levels: list[int]) -> int:
    A, b = build_equations(button_wirings, joltage_levels)
    num_buttons = len(button_wirings)
    
    c = [1] * num_buttons
    constraints = LinearConstraint(A, b, b)
    bounds = Bounds(lb=0, ub=float('inf'))
    integrality = [1] * num_buttons
    
    result = milp(c, constraints=constraints, bounds=bounds, integrality=integrality)
    return int(result.fun)


# Solvers

def solve_part1(input_path: str) -> int:
    lines = read_input(input_path)
    total = 0
    for line in lines:
        lights, button_wirings, _ = parse_line(line)
        lights_mask = lights_to_bitmask(lights)
        button_masks = create_button_masks(button_wirings)
        total += count_button_presses_for_lights(lights_mask, button_masks)
    return total


def solve_part2(input_path: str) -> int:
    lines = read_input(input_path)
    total = 0
    for line in lines:
        _, button_wirings, joltage_levels = parse_line(line)
        total += count_button_presses_for_joltage(button_wirings, joltage_levels)
    return total


if __name__ == "__main__":
    solution1 = solve_part1(puzzle_input)
    solution2 = solve_part2(puzzle_input)
    print(f"\n\nsolution part 1 : {solution1}")
    print(f"\nsolution part 2 : {solution2}")