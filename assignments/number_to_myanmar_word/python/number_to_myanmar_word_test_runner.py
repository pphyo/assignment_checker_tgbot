import sys
import re # For easier replacement
from number_to_myanmar_word import NumberToMyanmarWord

# Helper function to normalize "တစ်" to "တ" before major units
def normalize_prefix(word):
    # Use regex to replace "တစ်" followed by any unit name
    return re.sub(r'တစ်(ဆယ်|ရာ|ထောင်|သောင်း|သိန်း|သန်း|ကုဋေ)', r'တ\1', word)

def run_tests():
    solver = NumberToMyanmarWord()
    # Expected outputs use simplified grammar AND the "တ" prefix
    test_cases = [
        (0, "သုညကျပ်"), (5, "ငါးကျပ်"), (10, "တဆယ်ကျပ်"), (11, "တဆယ့်တစ်ကျပ်"),
        (25, "နှစ်ဆယ့်ငါးကျပ်"), (100, "တရာကျပ်"), (101, "တရာတစ်ကျပ်"),
        (110, "တရာတဆယ်ကျပ်"), (1000, "တထောင်ကျပ်"), (1001, "တထောင်တစ်ကျပ်"),
        (1234, "တထောင်နှစ်ရာသုံးဆယ့်လေးကျပ်"), (10000, "တသောင်းကျပ်"),
        (10101, "တသောင်းတရာတကျပ်"), (11000, "တသောင်းတထောင်ကျပ်"),
        (110101, "တသိန်းတသောင်းတရာတကျပ်"),
        (123456, "တသိန်းနှစ်သောင်းသုံးထောင်လေးရာငါးဆယ့်ခြောက်ကျပ်"),
        (1000000, "တသန်းကျပ်")
    ]

    passed_count = 0
    report = []
    print("===== Starting Automated Tests for NumberToMyanmarWord (Python) =====")

    for i, (input_val, expected_output) in enumerate(test_cases):
        actual_output = ""
        try:
            actual_output = solver.convert(input_val)
            report.append(f"Test Case #{i + 1}: Input '{input_val}'")
            report.append(f" -> Expected: \"{expected_output}\", Got: \"{actual_output}\"")

            # Normalize both before comparing
            normalized_expected = normalize_prefix(expected_output)
            normalized_actual = normalize_prefix(actual_output)

            if normalized_actual == normalized_expected:
                report.append(" -> ✅ PASS\n")
                passed_count += 1
            else:
                report.append(f" -> ❌ FAIL (Normalized: Expected '{normalized_expected}', Got '{normalized_actual}')\n")
        except Exception as e:
            report.append(f" -> ❌ ERROR: An exception occurred - {type(e).__name__}\n")

    # ... (Rest of the runner code: print report, summary, [SUMMARY] line) ...
    print("\n".join(report))
    print("===== Test Summary ====="); print(f"Total Tests: {len(test_cases)}"); print(f"Passed: {passed_count}"); print(f"Failed: {len(test_cases) - passed_count}"); print("========================")
    print(f"[SUMMARY]:{passed_count}:{len(test_cases)}")


if __name__ == "__main__":
    sys.path.append('.')
    run_tests()