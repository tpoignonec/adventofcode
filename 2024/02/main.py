# !/usr/bin/env python3
import os
import numpy as np


def read_input(file_path: str) -> list[list[int]]:
    """
    Reads a text file and returns its contents as a list of lists.

    Note: because each "report" has a varying number of levels...
    """
    absolute_file_path = \
        os.path.join(os.path.dirname(__file__), file_path)

    reports = []
    with open(absolute_file_path, 'r') as f:
        for line in f:
            # Split each line and convert to integers
            levels = [int(x) for x in line.strip().split()]
            reports.append(levels)

    return reports


def is_strictly_monotonic(arr: np.ndarray) -> bool:
    return np.all(np.diff(arr) > 0) or np.all(np.diff(arr) < 0)


def are_adjacent_levels_within_range(arr: np.ndarray, min_diff: int = 1, max_diff: int = 3) -> bool:
    diffs = np.abs(np.diff(arr))
    return np.all((diffs >= min_diff) & (diffs <= max_diff))


def is_safe(arr: np.ndarray) -> bool:
    return is_strictly_monotonic(arr) and \
           are_adjacent_levels_within_range(arr)


def solve_part1(data: list[list[int]]) -> int | None:
    """Number of safe reports

    Each row in the data represents a report of "levels".
    A report is considered "safe" if it meets the following conditions:"
    - Condition 1: strictly increasing or decreasing
    - Condition 2: any two adjacent levels differ by at least one and
      at most three
    """
    safe_count = 0
    for report_levels in data:
        if is_safe(np.asarray(report_levels)):
            safe_count += 1
    return safe_count


def solve_part2(data: list[list[int]]) -> int | None:
    """With "dampener"

    Same as part 1, but if remove any ONE level from the report makes
    it safe, then the report is also considered safe.
    """
    safe_count = 0
    for report_levels in data:
        if is_safe(np.asarray(report_levels)):
            safe_count += 1
        else:
            # Check if removing any one level makes it safe
            for i in range(len(report_levels)):
                modified_report = np.delete(np.asarray(report_levels), i)
                if is_safe(modified_report):
                    safe_count += 1
                    break
    return safe_count


def main():
    # Test with sample data first
    sample_data = read_input('sample.txt')
    print("Sample data length:", len(sample_data))

    # Part 1 test
    sample_result_1 = solve_part1(sample_data)
    expected_sample_result_1 = 2
    assert sample_result_1 == expected_sample_result_1, \
        f"Expected {expected_sample_result_1} but got {sample_result_1}"

    # Part 2 test
    sample_result_2 = solve_part2(sample_data)
    expected_sample_result_2 = 4
    assert sample_result_2 == expected_sample_result_2, \
        f"Expected {expected_sample_result_2} but got {sample_result_2}"

    # Load actual input data
    input_data = read_input('input.txt')
    print("Input data length:", len(input_data))

    # Solve problem with actual data
    result_1 = solve_part1(input_data)
    print(f"Part 1 -- Number of safe reports: {result_1}")

    result_2 = solve_part2(input_data)
    print(f"Part 2 -- Number of safe reports: {result_2}")


if __name__ == "__main__":
    main()