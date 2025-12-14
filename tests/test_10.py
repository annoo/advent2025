import pytest
from day10.solution import solve_part1, solve_part2, parse_line, read_input, count_button_presses, lights_to_bitmask, wiring_to_bitmask, create_button_masks

test_input_part1 = "day10/test_input.txt"
test_input_part2 = "day10/test_input.txt"  # Change if part 2 has different example


def test_parse_line():
    line = "[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}"
    lights, wirings = parse_line(line)
    
    assert lights == [False, True, True, False]
    assert wirings == [(3,), (1, 3), (2,), (2, 3), (0, 2), (0, 1)]


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


def test_amount_of_button_presses():
    lines = read_input(test_input_part1)
    
    for i, expected in [(0, 2), (1, 3), (2, 2)]:
        lights, wirings = parse_line(lines[i])
        target = lights_to_bitmask(lights)
        buttons = create_button_masks(wirings)
        assert count_button_presses(target, buttons) == expected


@pytest.mark.parametrize(
    "part, input_data, expected_output",
    [
        (1, test_input_part1, 7),  # Replace None with expected answer
        # (2, test_input_part2, None),  # Uncomment and add expected answer for part 2
    ],
)
def test_solve(part, input_data, expected_output):
    if part == 1:
        result = solve_part1(input_data)
    else:
        result = solve_part2(input_data)
    print(f"\n\n{result=}")
    assert result == expected_output