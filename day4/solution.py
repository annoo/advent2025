puzzle_input: str = "day4/input.txt"


def read_input(input_data: str) -> list[str]:
    if isinstance(input_data, str) and '\n' in input_data:
        lines = input_data.strip().split('\n')
    else:
        with open(input_data, "r") as file:
            lines = file.read().splitlines()
    return lines

DIRS_4 = [(0, 1), (0, -1), (1, 0), (-1, 0)]
DIRS_8 = [(dr, dc) for dr in [-1, 0, 1] for dc in [-1, 0, 1] if (dr, dc) != (0, 0)]

def count_adjacent(grid, position, directions=DIRS_8):
    rows, cols = len(grid), len(grid[0])
    r, c = position

    adjacent_rolls = 0

    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if (0 <= nr < rows and 
            0 <= nc < cols):
                neighbor = grid[nr][nc] # value of r,c
                if neighbor == '@':
                    adjacent_rolls += 1
    return adjacent_rolls

def remove_accessible_rolls(grid):
    rows, cols = len(grid), len(grid[0])
    new_grid = [list(row) for row in grid]

    removed = 0

    for r in range(rows):
        for c in range(cols):
            position = (r, c)
            space = grid[r][c]
            if space == '@' and count_adjacent(grid, position) < 4:
                new_grid[r][c] = '.'
                removed += 1
    
    return [''.join(row) for row in new_grid], removed


def solve_part1(input: str) -> int:
    grid = read_input(input)
    _, rolls_to_be_removed = remove_accessible_rolls(grid)
    return rolls_to_be_removed


def solve_part2(input: str) -> int:
    grid = read_input(input)
    total_removed = 0

    while True:
        grid, removed = remove_accessible_rolls(grid)
        if removed == 0:
            break
        total_removed += removed
    
    return total_removed


if __name__ == "__main__":
    solution1 = solve_part1(puzzle_input)
    solution2 = solve_part2(puzzle_input)
    print(f"\n\nsolution part 1 : {solution1}")
    print(f"\nsolution part 2 : {solution2}")

