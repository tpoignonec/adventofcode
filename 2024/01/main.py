# !/usr/bin/env python3
import os
import numpy as np


def read_input(file_path):
    """Reads a text file and returns its contents as a numpy array."""
    absolute_file_path = \
        os.path.join(os.path.dirname(__file__), file_path)
    return np.loadtxt(absolute_file_path)


def solve(data):
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


def main():
    # Test with sample data first
    sample_data = read_input('sample.txt')
    print("Sample data shape:", sample_data.shape)
    sample_result = solve(sample_data)
    expected_sample_result = 11
    assert sample_result == expected_sample_result, \
        f"Expected {expected_sample_result} but got {sample_result}"

    # Load actual input data
    input_data = read_input('input.txt')
    print("Input data shape:", input_data.shape)

    # Solve problem with actual data
    result = solve(input_data)
    print(f"Total distance: {result}")

if __name__ == "__main__":
    main()