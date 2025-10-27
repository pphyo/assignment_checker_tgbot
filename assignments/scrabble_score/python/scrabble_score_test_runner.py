import sys
from scrabble_score import ScrabbleScore # Import the student's class

def run_tests():
    solver = ScrabbleScore()
    # Test Cases: (word1, word2, expectedResultString)
    test_cases = [
        ("Question?", "Query", "One wins!"), ("Apple", "Banana", "Two wins!"),
        ("Programming", "Coding", "One wins!"), ("HELLO", "hello", "Tie!"),
        ("CS50", "Harvard", "Two wins!"), ("", "Empty", "Two wins!"),
        ("Points!", "Score?", "One wins!"), ("Tie", "Tie", "Tie!"),
        ("Test", "", "One wins!"), (None, "Word", "Two wins!"), # Test None
        ("Word", None, "One wins!"), (None, None, "Tie!")
    ]
    passed_count = 0
    report = []
    print("===== Starting Automated Tests for Scrabble Score Comparator (Python) =====")

    for i, (word1, word2, expected) in enumerate(test_cases):
        actual = "Error"
        input1_desc = "None" if word1 is None else f'"{word1}"'
        input2_desc = "None" if word2 is None else f'"{word2}"'
        case_identifier = f'Test Case #{i + 1}: Player 1({input1_desc}) vs Player 2({input2_desc})'
        try:
            # Call the updated method
            actual = solver.compare_scores(word1, word2)
            report.append(case_identifier)
            report.append(f' -> Expected: "{expected}", Got: "{actual}"')

            if actual == expected:
                report.append(" -> ✅ PASS\n")
                passed_count += 1
            else:
                report.append(" -> ❌ FAIL\n")
        except Exception as e:
            report.append(case_identifier)
            report.append(f" -> ❌ ERROR during comparison: {type(e).__name__}\n")

    print("\n".join(report))
    print("===== Test Summary ====="); print(f"Total Tests: {len(test_cases)}"); print(f"Passed: {passed_count}"); print(f"Failed: {len(test_cases) - passed_count}"); print("========================")
    print(f"[SUMMARY]:{passed_count}:{len(test_cases)}")

if __name__ == "__main__":
    sys.path.append('.')
    run_tests()