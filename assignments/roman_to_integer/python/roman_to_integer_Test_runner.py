import sys
sys.path.append('.')
from roman_to_integer import RomanToInteger

def run_tests():
    solver = RomanToInteger()

    test_cases = [
        ("III", 3),
        ("LVIII", 58),
        ("MCMXCIV", 1994),
        ("IX", 9),
        ("IV", 4),
        ("CM", 900),
    ]

    passed_count = 0
    report = []

    print("===== Starting Automated Tests for RomanToInteger (Python) =====")

    for i, (input_val, expected_output) in enumerate(test_cases):
        try:
            actual_output = solver.convert(input_val)

            report.append(f"Test Case #{i + 1}: Input '{input_val}'")
            report.append(f" -> Expected: {expected_output}, Got: {actual_output}")

            if actual_output == expected_output:
                report.append(" -> ✅ PASS\n")
                passed_count += 1
            else:
                report.append(" -> ❌ FAIL\n")
        except Exception as e:
            report.append(f"Test Case #{i + 1}: Input '{input_val}'")
            report.append(f" -> ❌ ERROR: {type(e).__name__}\n")

    print("\n".join(report))
    print("===== Test Summary =====")
    print(f"Total Tests: {len(test_cases)}")
    print(f"Passed: {passed_count}")
    print(f"Failed: {len(test_cases) - passed_count}")
    print("========================")

    print(f"[SUMMARY]:{passed_count}:{len(test_cases)}")

if __name__ == "__main__":
    run_tests()