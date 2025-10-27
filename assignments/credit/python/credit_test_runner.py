import sys
from credit import Credit # Import the student's class

def run_tests():
    solver = Credit()
    # Test Cases: (cardNumber, expectedResult)
    test_cases = [
        ("4062901840127322", "VISA"), ("4000000000000", "VISA"),
        ("378282246310005", "AMEX"), ("340000000000000", "AMEX"),
        ("5105105105105100", "MASTERCARD"), ("5555555555555555", "MASTERCARD"),
        ("4062901840127321", "INVALID"), ("378282246310006", "INVALID"),
        ("5105105105105101", "INVALID"), ("411122223333", "INVALID"),
        ("41112222333344445", "INVALID"), ("6011000000000000", "INVALID"),
        ("1234567890123", "INVALID"), (None, "INVALID"), ("", "INVALID"),
        ("abcde12345abcde", "INVALID")
    ]
    passed_count = 0
    report = []
    print("===== Starting Automated Tests for Credit Card Validator (Python) =====")

    for i, (input_num, expected) in enumerate(test_cases):
        actual = "Error"
        case_identifier = f'Test Case #{i + 1}: Input "{input_num}"'
        try:
            actual = solver.validate_credit_card(input_num)
            report.append(case_identifier)
            report.append(f' -> Expected: "{expected}", Got: "{actual}"')

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