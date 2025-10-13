import sys
from two_sum import TwoSum

def run_tests():
    """
    Runs a series of test cases against the student's TwoSum implementation.
    """
    solver = TwoSum()

    test_cases = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
    ]

    passed_count = 0
    report = []

    print("===== Starting Automated Tests for TwoSum (Python) =====")

    for i, (nums_input, target_input, expected_output) in enumerate(test_cases):
        try:
            actual_output = solver.solve(nums_input, target_input)

            if actual_output:
                actual_output.sort()
            expected_output.sort()

            report.append(f"Test Case #{i + 1}: Input nums={nums_input}, target={target_input}")
            report.append(f" -> Expected: {expected_output}, Got: {actual_output}")

            if actual_output == expected_output:
                report.append(" -> ✅ PASS\n")
                passed_count += 1
            else:
                report.append(" -> ❌ FAIL\n")

        except Exception as e:
            report.append(f"Test Case #{i + 1}: Input nums={nums_input}, target={target_input}")
            report.append(f" -> ❌ ERROR: An exception occurred - {type(e).__name__}\n")

    print("\n".join(report))
    print("===== Test Summary =====")
    print(f"Total Tests: {len(test_cases)}")
    print(f"Passed: {passed_count}")
    print(f"Failed: {len(test_cases) - passed_count}")
    print("========================")

    print(f"[SUMMARY]:{passed_count}:{len(test_cases)}")

if __name__ == "__main__":
    sys.path.append('.')
    run_tests()