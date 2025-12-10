puzzle_input: str = "day7/input.txt"
from collections import defaultdict


def read_input(input_data: str) -> list[str]:
    if isinstance(input_data, str) and '\n' in input_data:
        lines = input_data.strip().split('\n')
    else:
        with open(input_data, "r") as file:
            lines = file.read().splitlines()
    return lines

def solve_part1(input: str) -> int:
    lines = read_input(input)
    source_col = lines[0].index('S')
    splits = 0

    beams = {source_col}

    for row in range(2, len(lines), 2):
        new_beams = set()
        for pos in beams:
            if lines[row][pos] == '^':
                splits += 1
                new_beams.add(pos - 1)
                new_beams.add(pos + 1)
            else:
                new_beams.add(pos)
        beams = new_beams
    
    return splits

def solve_part2(input: str) -> int:
    lines = read_input(input)
    source_col = lines[0].index('S')

    timelines = defaultdict(int)
    timelines[source_col] = 1

    for row in range(2, len(lines), 2):
        new_timelines = defaultdict(int)
        for pos, count in timelines.items():
            if lines[row][pos] == '^':
                new_timelines[pos - 1] += count        
                new_timelines[pos + 1] += count      
            else:
                new_timelines[pos] += count
        timelines = new_timelines  
    
    return sum(timelines.values())


if __name__ == "__main__":
    solution1 = solve_part1(puzzle_input)
    solution2 = solve_part2(puzzle_input)
    print(f"\n\nsolution part 1 : {solution1}")
    print(f"\nsolution part 2 : {solution2}")