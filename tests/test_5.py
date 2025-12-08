import pytest
from day5.solution import solve_part1, solve_part2

test_input_part1 = "day5/test_input.txt"
test_input_part2 = "day5/test_input.txt"  # Change if part 2 has different example

@pytest.mark.parametrize(
    "part, input_data, expected_output",
    [
        (1, test_input_part1, 3),  # Replace None with expected answer
        (2, test_input_part2, 14),  # Uncomment and add expected answer for part 2
    ],
)
def test_solve(part, input_data, expected_output):
    if part == 1:
        result = solve_part1(input_data)
    else:
        result = solve_part2(input_data)
    print(f"\n\n{result=}")
    assert result == expected_output