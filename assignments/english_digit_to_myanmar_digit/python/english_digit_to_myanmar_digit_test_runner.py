import sys
from english_digit_to_myanmar_digit import EnglishDigitToMyanmarDigit

def run_tests():
    solver = EnglishDigitToMyanmarDigit()
    test_cases = [
        (0, "၀"), (9, "၉"), (10, "၁၀"), (11, "၁၁"), (1234, "၁၂၃၄"),
        (2314, "၂၃၁၄"), (987654321, "၉၈၇၆၅၄၃၂၁")
    ]
    passed_count = 0
    report = []
    print("===== Starting Automated Tests for EnglishDigitToMyanmarDigit (Python) =====")

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
            report.append(f" -> ❌ ERROR: An exception occurred - {type(e).__name__}\n")

    print("\n".join(report))
    print("===== Test Summary ====="); print(f"Total Tests: {len(test_cases)}"); print(f"Passed: {passed_count}"); print(f"Failed: {len(test_cases) - passed_count}"); print("========================")
    print(f"[SUMMARY]:{passed_count}:{len(test_cases)}")

if __name__ == "__main__":
    sys.path.append('.')
    run_tests()