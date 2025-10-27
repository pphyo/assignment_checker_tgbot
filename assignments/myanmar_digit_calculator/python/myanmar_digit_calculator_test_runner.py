import sys
from myanmar_digit_calculator import MyanmarCalculator

def run_tests():
    solver = MyanmarCalculator()
    test_cases = [
        ("၁၂၃", "၄၅၆", '+', "၅၇၉"),
        ("၁၀၀", "၁၀", '-', "၉၀"),
        ("၂၀", "၅", '*', "၁၀၀"),
        ("၂၁", "၅", '/', "၄"),
        ("၁၀", "၀", '/', "Error: Division by zero"),
        ("၀", "၅", '+', "၅"),
        ("၅", "၀", '*', "၀"),
        ("၉၈၇", "၁၂၃", '+', "၁၁၁၀"),
        ("၁၀", "၂၀", '-', "-၁၀") # Python's str() handles negative correctly
    ]
    passed_count = 0
    report = []
    print("===== Starting Automated Tests for MyanmarCalculator (Python) =====")

    for i, (n1, n2, op, expected) in enumerate(test_cases):
        actual = ""
        try:
            actual = solver.calculate(n1, n2, op)
            report.append(f"Test Case #{i + 1}: Input '{n1}' {op} '{n2}'")
            report.append(f" -> Expected: \"{expected}\", Got: \"{actual}\"")

            if actual == expected:
                report.append(" -> ✅ PASS\n")
                passed_count += 1
            else:
                report.append(" -> ❌ FAIL\n")
        except Exception as e:
            report.append(f"Test Case #{i + 1}: Input '{n1}' {op} '{n2}'")
            report.append(f" -> ❌ ERROR: An exception occurred - {type(e).__name__}\n")

    print("\n".join(report))
    print("===== Test Summary ====="); print(f"Total Tests: {len(test_cases)}"); print(f"Passed: {passed_count}"); print(f"Failed: {len(test_cases) - passed_count}"); print("========================")
    print(f"[SUMMARY]:{passed_count}:{len(test_cases)}")

if __name__ == "__main__":
    sys.path.append('.')
    run_tests()