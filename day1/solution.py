puzzle_input = "day1/input.txt"


def read_input(input_data):
    if isinstance(input_data, str) and '\n' in input_data:
        lines = input_data.strip().split('\n')
    else:
        with open(input_data, "r") as file:
            lines = file.readlines()
    return lines

def move_pointer(pointer, direction, steps, size=100):
    if direction == 'L':
        return (pointer - steps) % size
    else:
        return (pointer + steps) % size
    
def step_through(pointer, direction, steps, size=100):
    hits = 0
    
    for _ in range(steps):
        if direction == 'L':
            pointer = (pointer - 1) % size
        else:
            pointer = (pointer + 1) % size
        if pointer == 0:
            hits += 1
    return pointer, hits

def solve_part1(puzzle_input):
    lines = read_input(puzzle_input)
    nbr_of_times_pointing_to_zero = 0
    pointer = 50

    for line in lines:
        direction = line[0]
        steps = int(line[1:])

        pointer = move_pointer(pointer, direction=direction, steps=steps)
        if pointer == 0:
            nbr_of_times_pointing_to_zero += 1
        

    return nbr_of_times_pointing_to_zero


def solve_part2(puzzle_input):
    lines = read_input(puzzle_input)
    nbr_of_times_pointing_to_zero = 0
    pointer = 50

    for line in lines:
        direction = line[0]
        steps = int(line[1:])

        pointer, hits = step_through(pointer, direction=direction, steps=steps)
        nbr_of_times_pointing_to_zero += hits

    return nbr_of_times_pointing_to_zero


if __name__ == "__main__":
    solution1 = solve_part1(puzzle_input)
    solution2 = solve_part2(puzzle_input)
    print(f"\n\nsolution part 1 : {solution1}")
    print(f"\nsolution part 2 : {solution2}")