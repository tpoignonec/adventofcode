# !/usr/bin/env python3
import os
import numpy as np


def read_input(file_path):
    """Reads a text file and returns its contents as a numpy array."""
    absolute_file_path = \
        os.path.join(os.path.dirname(__file__), file_path)
    return np.loadtxt(absolute_file_path)


def solve_part1(data):
    """Calculate total distance between sorted lists"""
    # Split the data into two columns (left and right lists)
    left_list = data[:, 0]
    right_list = data[:, 1]

    # Sort both lists
    left_sorted = np.sort(left_list)
    right_sorted = np.sort(right_list)

    # Calculate distances (absolute differences)
    distances = np.abs(left_sorted - right_sorted)

    # Return the sum of all distances
    return np.sum(distances)


def solve_part2(data):
    """Placeholder for part 2 solution."""
    return 0


def main():
    # Test with sample data first
    sample_data = read_input('sample.txt')
    print("Sample data shape:", sample_data.shape)

    # Part 1 test
    sample_result_1 = solve_part1(sample_data)
    expected_sample_result_1 = 11
    assert sample_result_1 == expected_sample_result_1, \
        f"Expected {expected_sample_result_1} but got {sample_result_1}"

    # Part 2 test
    sample_result_2 = solve_part2(sample_data)
    expected_sample_result_2 = 31
    assert sample_result_2 == expected_sample_result_2, \
        f"Expected {expected_sample_result_2} but got {sample_result_2}"

    # Load actual input data
    input_data = read_input('input.txt')
    print("Input data shape:", input_data.shape)

    # Solve problem with actual data
    result_1 = solve_part1(input_data)
    print(f"Part 1 -- Total distance: {result_1}")

    result_2 = solve_part2(input_data)
    print(f"Part 2 -- Total distance: {result_2}")

if __name__ == "__main__":
    main()