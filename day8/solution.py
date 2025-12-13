from typing import TypeAlias
from collections import Counter

puzzle_input: str = "day8/input.txt"

Point: TypeAlias = tuple[int, int, int]


def read_input(input_data: str) -> list[str]:
    if isinstance(input_data, str) and '\n' in input_data:
        lines = input_data.strip().split('\n')
    else:
        with open(input_data, "r") as file:
            lines = file.read().splitlines()
    return lines


def parse_points(lines: list[str]) -> list[Point]:
    return [tuple(int(n) for n in line.split(',')) for line in lines]


def calculate_distance(p1: Point, p2: Point) -> int:
    return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 + (p1[2]-p2[2])**2


def multiply_x(p1: Point, p2: Point) -> int:
    return p1[0] * p2[0]


def find(x: int, parent: list[int]) -> int:
    """Find the root of x's group."""
    root = x
    # Follow the chain until we find the root (points to itself)
    while parent[root] != root:
        root = parent[root]
    
    # Path compression: shortcut everyone to point directly to root
    while parent[x] != root:
        next_x = parent[x]
        parent[x] = root
        x = next_x
    
    return root


def union(a: int, b: int, parent: list[int]) -> bool:
    """Merge the groups containing a and b. Returns True if they were different groups."""
    root_a = find(a, parent)
    root_b = find(b, parent)
    if root_a != root_b:
        # Merge: root_a now points to root_b
        parent[root_a] = root_b
        return True  # groups were merged
    return False  # already in same group


def connected(a: int, b: int, parent: list[int]) -> bool:
    """Check if two nodes are in the same group."""
    return find(a, parent) == find(b, parent)


def solve_part1(input_path: str) -> int:
    
    lines = read_input(input_path)
    points = parse_points(lines)
    n = len(points)
    
    # Each node starts as its own root (parent[i] = i)
    parent = list(range(n))
    
    # Generate all possible edges with distances
    # (distance, node_a, node_b)
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            dist = calculate_distance(points[i], points[j])
            edges.append((dist, i, j))
    
    # Sort by distance (closest first)
    edges.sort()
    
    # Process edges: 10 for test (20 nodes), 1000 for real input (1000 nodes)
    num_connections = 10 if n == 20 else 1000
    for dist, a, b in edges[:num_connections]:
        union(a, b, parent)
    
    # Count how many nodes in each circuit
    circuit_sizes = Counter(find(i, parent) for i in range(n))
    
    # Get the 3 largest sizes and multiply
    largest_three = sorted(circuit_sizes.values(), reverse=True)[:3]
    
    return largest_three[0] * largest_three[1] * largest_three[2]

def solve_part2(input_path: str) -> int:
    lines = read_input(input_path)
    points = parse_points(lines)
    n = len(points)
    
    # Each node starts as its own root (parent[i] = i)
    parent = list(range(n))
    
    # Generate all possible edges with distances
    # (distance, node_a, node_b)
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            dist = calculate_distance(points[i], points[j])
            edges.append((dist, i, j))
    
    edges.sort()

    last_a, last_b = None, None
    for dist, a, b in edges:

        if union(a, b, parent):  # True = they were in different circuits
            # Track the last edge that actually merged two circuits
            last_a, last_b = a, b
    
    return multiply_x(points[last_a], points[last_b])




if __name__ == "__main__":
    solution1 = solve_part1(puzzle_input)
    solution2 = solve_part2(puzzle_input)
    print(f"\n\nsolution part 1 : {solution1}")
    print(f"\nsolution part 2 : {solution2}")