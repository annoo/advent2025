import pytest
from day10.solution import solve_part1, solve_part2, parse_line, read_input, count_button_presses_for_lights, count_button_presses_for_joltage, lights_to_bitmask, wiring_to_bitmask, create_button_masks, build_button_matrix, build_equations

test_input_part1 = "day10/test_input.txt"
test_input_part2 = "day10/test_input.txt"  # Change if part 2 has different example


def test_parse_line():
    line = "[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}"
    lights, wirings, joltage = parse_line(line)
    
    assert lights == [False, True, True, False]
    assert wirings == [(3,), (1, 3), (2,), (2, 3), (0, 2), (0, 1)]
    assert joltage == [3, 5, 4, 7]


def test_lights_to_bitmask():
    # [False, True, True, False] -> bits 1 and 2 set -> 0b0110 = 6
    assert lights_to_bitmask([False, True, True, False]) == 0b0110
    assert lights_to_bitmask([True, False, False, False]) == 0b0001
    assert lights_to_bitmask([True, True, True, True]) == 0b1111


def test_wiring_to_bitmask():
    # (1, 3) -> bits 1 and 3 set -> 0b1010 = 10
    assert wiring_to_bitmask((1, 3)) == 0b1010
    assert wiring_to_bitmask((3,)) == 0b1000
    assert wiring_to_bitmask((0, 2)) == 0b0101


def test_amount_of_button_presses_for_lights():
    lines = read_input(test_input_part1)
    
    for i, expected in [(0, 2), (1, 3), (2, 2)]:
        lights, wirings, _ = parse_line(lines[i])
        target = lights_to_bitmask(lights)
        buttons = create_button_masks(wirings)
        assert count_button_presses_for_lights(target, buttons) == expected


def test_amount_of_button_presses_for_joltage():
    lines = read_input(test_input_part1)
    
    for i, expected in [(0, 10), (1, 12), (2, 11)]:
        _, button_wirings, joltage_levels = parse_line(lines[i])
        result = count_button_presses_for_joltage(button_wirings, joltage_levels)
        assert result == expected


def test_build_button_matrix():
    """Matrix[counter][button] = 1 if button affects counter, else 0"""
    # [.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
    # 4 counters, 6 buttons
    button_wirings = [(3,), (1, 3), (2,), (2, 3), (0, 2), (0, 1)]
    num_counters = 4
    
    matrix = build_button_matrix(button_wirings, num_counters)
    
    # Button 0: (3) affects counter 3 only
    assert matrix[3][0] == 1
    assert matrix[0][0] == 0
    
    # Button 1: (1,3) affects counters 1 and 3
    assert matrix[1][1] == 1
    assert matrix[3][1] == 1
    assert matrix[0][1] == 0
    
    # Button 4: (0,2) affects counters 0 and 2
    assert matrix[0][4] == 1
    assert matrix[2][4] == 1


def test_build_equations():
    """
    Each equation represents: sum of (button presses * coefficient) = target
    Where coefficient is 1 if button affects that counter, 0 otherwise.
    
    Returns matrix A and vector b for: Ax = b
    Where x = [presses_button0, presses_button1, ...]
    """
    # [.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
    button_wirings = [(3,), (1, 3), (2,), (2, 3), (0, 2), (0, 1)]
    joltage_levels = [3, 5, 4, 7]
    
    A, b = build_equations(button_wirings, joltage_levels)
    
    # b is the target vector
    assert b == [3, 5, 4, 7]
    
    # A[counter] = coefficients for each button
    # Counter 0: affected by buttons (0,2) at idx 4, (0,1) at idx 5
    assert A[0] == [0, 0, 0, 0, 1, 1]
    
    # Counter 1: affected by buttons (1,3) at idx 1, (0,1) at idx 5
    assert A[1] == [0, 1, 0, 0, 0, 1]
    
    # Counter 2: affected by buttons (2) at idx 2, (2,3) at idx 3, (0,2) at idx 4
    assert A[2] == [0, 0, 1, 1, 1, 0]
    
    # Counter 3: affected by buttons (3) at idx 0, (1,3) at idx 1, (2,3) at idx 3
    assert A[3] == [1, 1, 0, 1, 0, 0]


@pytest.mark.parametrize(
    "part, input_data, expected_output",
    [
        (1, test_input_part1, 7),  # Replace None with expected answer
        (2, test_input_part2, 33),  # Uncomment and add expected answer for part 2
    ],
)
def test_solve(part, input_data, expected_output):
    if part == 1:
        result = solve_part1(input_data)
    else:
        result = solve_part2(input_data)
    print(f"\n\n{result=}")
    assert result == expected_output