import sys
from integer_to_roman import IntegerToRoman

def run_tests():
    solver = IntegerToRoman()

    test_cases = [
        (3, "III"),
        (4, "IV"),
        (9, "IX"),
        (58, "LVIII"),
        (1994, "MCMXCIV"),
        (3749, "MMMDCCXLIX"),
        (3999, "MMMCMXCIX"),
    ]

    passed_count = 0
    report = []

    print("===== Starting Automated Tests for IntegerToRoman (Python) =====")

    for i, (input_val, expected_output) in enumerate(test_cases):
        try:
            actual_output = solver.convert(input_val)

            report.append(f"Test Case #{i + 1}: Input '{input_val}'")
            report.append(f" -> Expected: \"{expected_output}\", Got: \"{actual_output}\"")

            if actual_output == expected_output:
                report.append(" -> ✅ PASS\n")
                passed_count += 1
            else:
                report.append(" -> ❌ FAIL\n")

        except Exception as e:
            report.append(f"Test Case #{i + 1}: Input '{input_val}'")
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