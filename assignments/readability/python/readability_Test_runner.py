import sys
from readability import Readability # Import the student's class

def run_tests():
    solver = Readability()
    # Test Cases: (inputText, expectedGradeString)
    test_cases = [
        ("One fish. Two fish. Red fish. Blue fish.", "Before Grade 1"),
        ("Would you like them here or there? I would not like them here or there. I would not like them anywhere.", "Grade 2"),
        ("Congratulations! Today is your day. You're off to Great Places! You're off and away!", "Grade 3"),
        ("Harry Potter was a highly unusual boy in many ways. For one thing, he hated the summer holidays more than any other time of year. For another, he really wanted to do his homework, but was forced to do it in secret, in the dead of the night. And he also happened to be a wizard.", "Grade 5"),
        ("A large phone book enables you to call anybody. The reason is that it contains the numbers of everybody.", "Grade 9"),
        ("It was a bright cold day in April, and the clocks were striking thirteen. Winston Smith, his chin nuzzled into his breast in an effort to escape the vile wind, slipped quickly through the glass doors of Victory Mansions, though not quickly enough to prevent a swirl of gritty dust from entering along with him.", "Grade 8"),
        ("Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, 'and what is the use of a book,' thought Alice 'without pictures or conversation?'", "Grade 8"),
        ("There are more things in Heaven and Earth, Horatio, than are dreamt of in your philosophy.", "Grade 9"),
        ("It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife.", "Grade 12"),
        ("A beginning is the time for taking the most delicate care that balances are correct.", "Grade 11"),
        ("", "Before Grade 1"),
        ("One.", "Before Grade 1"),
        ("aaaaaaaaaa.", "Before Grade 1"),
        ("a a a. a a a? a a a!", "Before Grade 1"),
        ("This sentence is grade sixteen plus.", "Grade 16+")
    ]
    passed_count = 0
    report = []
    print("===== Starting Automated Tests for Readability (Python) =====")

    for i, (input_text, expected) in enumerate(test_cases):
        actual = "Error"
        case_identifier = f'Test Case #{i + 1}: Input "{input_text[:20]}..."'
        try:
            actual = solver.check_text(input_text)
            report.append(case_identifier)
            report.append(f' -> Expected: "{expected}"')
            report.append(f' ->      Got: "{actual}"')

            if actual == expected:
                report.append(" -> ✅ PASS\n")
                passed_count += 1
            else:
                report.append(" -> ❌ FAIL\n")
        except Exception as e:
            report.append(case_identifier)
            report.append(f" -> ❌ ERROR during calculation: {type(e).__name__}\n")

    print("\n".join(report))
    print("===== Test Summary ====="); print(f"Total Tests: {len(test_cases)}"); print(f"Passed: {passed_count}"); print(f"Failed: {len(test_cases) - passed_count}"); print("========================")
    print(f"[SUMMARY]:{passed_count}:{len(test_cases)}")

if __name__ == "__main__":
    sys.path.append('.')
    run_tests()