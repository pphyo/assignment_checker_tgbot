import sys
from binary_art_converter import BinaryArtConverter # Import the student's class

def run_tests():
    solver = BinaryArtConverter()
    test_cases = [
        ("Hi", "⚫⚪⚫⚫⚪⚫⚫⚫\n⚫⚪⚪⚫⚫⚪⚫⚪"),
        ("A", "⚫⚪⚫⚫⚫⚫⚫⚪"),
        ("z", "⚫⚪⚪⚪⚪⚫⚪⚫"),
        ("", ""),
        ("1", "⚫⚫⚪⚪⚫⚫⚫⚪"),
        ("Hello", "⚫⚪⚫⚫⚪⚫⚫⚫\n⚫⚪⚪⚫⚫⚪⚫⚪\n⚫⚪⚪⚫⚪⚪⚫⚫\n⚫⚪⚪⚫⚪⚪⚫⚫\n⚫⚪⚪⚫⚪⚪⚪⚪")
    ]
    passed_count = 0
    report = []
    print("===== Starting Automated Tests for BinaryArtConverter (Python) =====")

    for i, (input_text, expected) in enumerate(test_cases):
        actual = ""
        case_identifier = f'Test Case #{i + 1}: Input "{input_text}"'
        try:
            actual = solver.convert_to_binary_art(input_text)
            report.append(case_identifier)

            if actual == expected:
                report.append(f" -> Expected:\n{expected}")
                report.append(f" ->      Got:\n{actual}")
                report.append(" -> ✅ PASS\n")
                passed_count += 1
            else:
                report.append(f" -> Expected:\n{expected}")
                report.append(f" ->      Got:\n{actual}")
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