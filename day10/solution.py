from itertools import combinations
from functools import reduce

puzzle_input: str = "day10/input.txt"


def read_input(input_data: str) -> list[str]:
    if isinstance(input_data, str) and '\n' in input_data:
        lines = input_data.strip().split('\n')
    else:
        with open(input_data, "r") as file:
            lines = file.read().splitlines()
    return lines


def parse_line(line: str) -> tuple[list[bool], list[tuple]]:
    _, rest = line.split('[', 1)
    lights_str, rest = rest.split(']', 1)
    
    indicator_lights = [c == '#' for c in lights_str]
    
    tuples_part, _ = rest.split('{', 1)
    
    button_wirings = []
    for part in tuples_part.split('('):
        if ')' in part:
            content = part.split(')')[0]
            nums = tuple(int(x) for x in content.split(','))
            button_wirings.append(nums)
    
    return indicator_lights, button_wirings


def lights_to_bitmask(lights: list[bool]) -> int:
    """Convert [False, True, True, False] -> 0b0110 (= 6)"""
    mask = 0
    for i, on in enumerate(lights):
        if on:
            mask |= (1 << i)
    return mask


def wiring_to_bitmask(wiring: tuple) -> int:
    """Convert (1, 3) -> 0b1010 (bits 1 and 3 set)"""
    mask = 0
    for i in wiring:
        mask |= (1 << i)
    return mask


def create_button_masks(button_wirings):
    buttons = set()
    for button in button_wirings:
        button_mask = wiring_to_bitmask(button)
        buttons.add(button_mask)
    return buttons
    


def count_button_presses(lights: int, buttons: set[int]) -> int:
    press_count = 0
    max_tries = len(buttons) + 1

    for i in range(max_tries):
        press_count = i
        for combo in combinations(buttons, i):
            result = reduce(lambda a, b: a ^ b, combo, 0)
            if result == lights:
                return press_count


def solve_part1(input_path: str) -> int:
    lines = read_input(input_path)
    total_presses = 0

    for line in lines:
        indicator_lights, button_wirings = parse_line(line)
        lights_mask = lights_to_bitmask(indicator_lights)
        button_masks = create_button_masks(button_wirings)
        press = count_button_presses(lights_mask, button_masks)
        total_presses += press

    return total_presses


def solve_part2(input: str) -> int:
    return 0


if __name__ == "__main__":
    solution1 = solve_part1(puzzle_input)
    solution2 = solve_part2(puzzle_input)
    print(f"\n\nsolution part 1 : {solution1}")
    print(f"\nsolution part 2 : {solution2}")