import pytest
from day6.solution import solve_part1, solve_part2

test_input_part1 = "day6/test_input.txt"
test_input_part2 = "day6/test_input.txt"  # Change if part 2 has different example

@pytest.mark.parametrize(
    "part, input_data, expected_output",
    [
        (1, test_input_part1, 4277556),  # Replace None with expected answer
        (2, test_input_part2, 3263827),  # Uncomment and add expected answer for part 2
    ],
)
def test_solve(part, input_data, expected_output):
    if part == 1:
        result = solve_part1(input_data)
    else:
        result = solve_part2(input_data)
    print(f"\n\n{result=}")
    assert result == expected_output