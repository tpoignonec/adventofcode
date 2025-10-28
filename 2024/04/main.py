# !/usr/bin/env python3
import os
import numpy as np


def read_input(file_path: str) -> np.ndarray:
    """Reads a text file and returns its contents as a numpy array of characters."""
    absolute_file_path = \
        os.path.join(os.path.dirname(__file__), file_path)

    with open(absolute_file_path, 'r') as f:
        lines = [line.strip() for line in f.readlines()]

    # Convert to 2D numpy array of characters
    return np.array([list(line) for line in lines], dtype='U1')


def get_valid_lines(data: np.ndarray) -> np.ndarray:
    """From a 2D grid, get ALL valid lines (rows, columns, diagonals)"""

    valid_lines = []

    # Get all rows, columns, and diagonals
    valid_lines.extend(data.tolist())
    valid_lines.extend(data.T.tolist())
    valid_lines.extend([data.diagonal(i).tolist() for i in range(-data.shape[0]+1, data.shape[1])])
    valid_lines.extend([np.fliplr(data).diagonal(i).tolist() for i in range(-data.shape[0]+1, data.shape[1])])

    # Get reversed versions as well
    valid_lines.extend([list(reversed(line)) for line in valid_lines])

    return valid_lines


def solve_part1(data: np.ndarray) -> int | None:
    """Find occurrences of 'XMAS' words"""
    xmas_pattern = 'XMAS'
    valid_lines = get_valid_lines(data)
    xmas_count = 0
    for line in valid_lines:
        line_string = ''.join(line)
        xmas_count += line_string.count(xmas_pattern)
    return xmas_count


def solve_part2(data: np.ndarray) -> int | None:
    """???"""
    return None


def main():
    # Test with sample data first
    sample_data = read_input('sample.txt')
    print("Sample data:\n", sample_data)

    # Part 1 test
    sample_result_1 = solve_part1(sample_data)
    expected_sample_result_1 = 18
    assert sample_result_1 == expected_sample_result_1, \
        f"Expected {expected_sample_result_1} but got {sample_result_1}"

    # # Part 2 test
    # sample_result_2 = solve_part2(sample_data)
    # expected_sample_result_2 = 0
    # assert sample_result_2 == expected_sample_result_2, \
    #     f"Expected {expected_sample_result_2} but got {sample_result_2}"

    # Load actual input data
    input_data = read_input('input.txt')
    print("Input data shape:", input_data.shape)

    # Solve problem with actual data
    result_1 = solve_part1(input_data)
    print(f"Part 1 -- XMAS occurrences: {result_1}")

    result_2 = solve_part2(input_data)
    print(f"Part 2 -- ??? : {result_2}")

if __name__ == "__main__":
    main()