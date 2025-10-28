# !/usr/bin/env python3
import os
import re


def read_input(file_path: str) -> str:
    """
    Reads a text file
    """
    absolute_file_path = \
        os.path.join(os.path.dirname(__file__), file_path)

    with open(absolute_file_path, 'r') as f:
        return f.read()


def solve_part1(data: str) -> int | None:
    """Find and evaluate all multiplication expressions"""
    mul_expr_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    mul_exprs = re.findall(mul_expr_pattern, data)
    print(f"Found {len(mul_exprs)} multiplication expressions")
    return sum(int(x) * int(y) for x, y in mul_exprs)


def solve_part2(data: str, verbose: bool = False) -> int | None:
    """Idem, but 'do' and 'don't' can activate/ignore multiplications"""

    # This time, we parse for instructions: mul(...), do() and do_not()
    instr_pattern = r"(do\(\)|don't\(\)|mul\((\d{1,3}),(\d{1,3})\))"
    instructions = re.findall(instr_pattern, data)
    print(f"Found {len(instructions)} instructions")

    # Track whether multiplications are active
    mul_active = True
    total = 0

    for instr in instructions:
        match instr[0]:
            case "do()":
                if verbose:
                    print("Enabling subsequent multiplications")
                mul_active = True
            case "don't()":
                if verbose:
                    print("Ignoring subsequent multiplications")
                mul_active = False
            case _:
                # Only mul(...) remains
                if mul_active:
                    if verbose:
                        print(f"Evaluating: {instr[0]}")
                    total += int(instr[1]) * int(instr[2])

    return total


def main():
    # Test with sample data first
    sample_data = read_input('sample.txt')
    print("Sample data: " + sample_data)

    # Part 1 test
    sample_result_1 = solve_part1(sample_data)
    expected_sample_result_1 = 161
    assert sample_result_1 == expected_sample_result_1, \
        f"Expected {expected_sample_result_1} but got {sample_result_1}"

    # Part 2 test
    sample_data_2 = read_input('sample_2.txt')
    print("Sample data: " + sample_data_2)
    sample_result_2 = solve_part2(sample_data_2)
    expected_sample_result_2 = 48
    assert sample_result_2 == expected_sample_result_2, \
        f"Expected {expected_sample_result_2} but got {sample_result_2}"

    # Load actual input data
    input_data = read_input('input.txt')

    # Solve problem with actual data
    result_1 = solve_part1(input_data)
    print(f"Part 1 -- result: {result_1}")

    result_2 = solve_part2(input_data)
    print(f"Part 2 -- result: {result_2}")


if __name__ == "__main__":
    main()