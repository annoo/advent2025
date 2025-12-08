puzzle_input: str = "day5/input.txt"


def read_input(input_data: str) -> list[str]:
    if isinstance(input_data, str) and '\n' in input_data:
        lines = input_data.strip().split('\n')
    else:
        with open(input_data, "r") as file:
            lines = file.read().splitlines()
    return lines

def split_input(lines):
    split_index = lines.index('')
    part1_lines = lines[:split_index]
    part2_lines = lines[split_index + 1:]
    return part1_lines, part2_lines


def make_range(ID_range):
    start, stop = ID_range.split('-')
    return int(start), int(stop)


def merge_ranges(ranges):
    if not ranges:
        return []
    
    sorted_ranges = sorted(ranges, key=lambda x: x[0])
    
    merged = [sorted_ranges[0]]
    for current_start, current_stop in sorted_ranges[1:]:
        last_start, last_stop = merged[-1]
        
        if current_start <= last_stop + 1:
            merged[-1] = (last_start, max(last_stop, current_stop))
        else:
            merged.append((current_start, current_stop))
    
    return merged


def solve_part1(input: str) -> int:
    content = read_input(input)
    fresh_ingredients, available_ingredients = split_input(content)

    number_of_fresh_ingredients = 0
    for ingredient in available_ingredients:
        ingredient_num = int(ingredient)
        for fresh_range in fresh_ingredients:
            start, stop = make_range(fresh_range)
            if start <= ingredient_num <= stop:
                number_of_fresh_ingredients += 1
                break
    return number_of_fresh_ingredients


def solve_part2(input: str) -> int:
    content = read_input(input)
    fresh_ingredients, _ = split_input(content)
    
    parsed_ranges = [make_range(r) for r in fresh_ingredients]
    merged = merge_ranges(parsed_ranges)
    
    total_fresh_ingredients = 0
    for start, stop in merged:
        total_fresh_ingredients += stop - start + 1

    return total_fresh_ingredients

if __name__ == "__main__":
    solution1 = solve_part1(puzzle_input)
    solution2 = solve_part2(puzzle_input)
    print(f"\n\nsolution part 1 : {solution1}")
    print(f"\nsolution part 2 : {solution2}")