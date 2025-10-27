import sys
from cash_counting import CashCounting # Import the student's class

def run_tests():
    solver = CashCounting()
    # Corrected Test Cases: (input_amount, expected_note_count)
    test_cases = [
        (70, 3), (63, 5), (47, 5), (268, 6), (10000, 1),
        (15, 1), (14, 5), (29, 6), (0, 0), (1, 1),
        (4, 4), (5, 1), (9, 5), (10, 1), (12345, 8)
    ]
    passed_count = 0
    report = []
    print("===== Starting Automated Tests for Cash Change (Python) =====")

    for i, (input_amount, expected) in enumerate(test_cases):
        actual = -1
        case_identifier = f"Test Case #{i + 1}: Input amount={input_amount}"
        try:
            actual = solver.calculate_notes(input_amount)
            report.append(case_identifier)
            report.append(f" -> Expected: {expected}, Got: {actual}")

            if actual == expected:
                report.append(" -> ✅ PASS\n")
                passed_count += 1
            else:
                report.append(" -> ❌ FAIL\n")
        except Exception as e:
            report.append(case_identifier)
            report.append(f" -> ❌ ERROR: An exception occurred - {type(e).__name__}\n")

    print("\n".join(report))
    print("===== Test Summary ====="); print(f"Total Tests: {len(test_cases)}"); print(f"Passed: {passed_count}"); print(f"Failed: {len(test_cases) - passed_count}"); print("========================")
    print(f"[SUMMARY]:{passed_count}:{len(test_cases)}")

if __name__ == "__main__":
    sys.path.append('.')
    run_tests()