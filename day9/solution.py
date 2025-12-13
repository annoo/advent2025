from typing import TypeAlias
from itertools import combinations
from shapely.geometry import Polygon, box


puzzle_input: str = "day9/input.txt"


Tile: TypeAlias = tuple[int, int]


def read_input(input_data: str) -> list[str]:
    if isinstance(input_data, str) and '\n' in input_data:
        lines = input_data.strip().split('\n')
    else:
        with open(input_data, "r") as file:
            lines = file.read().splitlines()
    return lines


def parse_2D_coordinates(lines: list[str]) -> list[Tile]:
    return [tuple(int(n) for n in line.split(',')) for line in lines]


def calc_area(a: Tile, b: Tile) -> int:
    x1, y1 = a
    x2, y2 = b
    width = abs(x2 - x1) + 1  # +1 because tiles are inclusive
    height = abs(y2 - y1) + 1 
    return width * height


def solve_part1(input_path: str) -> int:
    lines = read_input(input_path)
    tiles = parse_2D_coordinates(lines)

    return max(calc_area(a, b) for a, b in combinations(tiles, 2))


def solve_part2(input_path: str) -> int:
    # had a look at RAY CASTING, interesting, but too complicated for me atm
    lines = read_input(input_path)
    red_tiles = parse_2D_coordinates(lines)
    
    polygon = Polygon(red_tiles)
    
    max_area = 0
    
    for tile_a, tile_b in combinations(red_tiles, 2):
        x1, y1 = tile_a
        x2, y2 = tile_b
        
        # Create rectangle from two opposite corners, 
        # regardless from with which point you start looking (up/right or low/left)
        rectangle = box(min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2))
        
        if polygon.covers(rectangle):
            area = calc_area(tile_a, tile_b)
            max_area = max(area, max_area)
    
    return max_area


if __name__ == "__main__":
    solution1 = solve_part1(puzzle_input)
    solution2 = solve_part2(puzzle_input)
    print(f"\n\nsolution part 1 : {solution1}")
    print(f"\nsolution part 2 : {solution2}")