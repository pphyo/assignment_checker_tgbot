import sys
from caesar_cipher import CaesarCipher # Import the student's class

def run_tests():
    solver = CaesarCipher()
    # Test Cases: (plainText, key, expectedCipherText)
    test_cases = [
        ("Hello, World!", 1, "Ifmmp, Xpsme!"),
        ("xyz", 3, "abc"), ("XYZ", 3, "ABC"),
        ("Be sure to drink your Ovaltine!", 13, "Or fher gb qevax lbhe Binygvar!"),
        ("Ciphering.", 26, "Ciphering."), ("middle-Outz", 2, "okffng-Qwvb"),
        ("A", 0, "A"), ("Z", 1, "A"), ("a", 25, "z"),
        ("123 ABC xyz .,!", 5, "123 FGH cde .,!"), ("", 10, ""),
        ("Test", 52, "Test")
    ]
    passed_count = 0
    report = []
    print("===== Starting Automated Tests for Caesar Cipher (Python) =====")

    for i, (plain_text, key, expected) in enumerate(test_cases):
        actual = "Error"
        case_identifier = f'Test Case #{i + 1}: Input "{plain_text}", Key={key}'
        try:
            actual = solver.encode_text(plain_text, key)
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
            report.append(f" -> ❌ ERROR during encryption: {type(e).__name__}\n")

    print("\n".join(report))
    print("===== Test Summary ====="); print(f"Total Tests: {len(test_cases)}"); print(f"Passed: {passed_count}"); print(f"Failed: {len(test_cases) - passed_count}"); print("========================")
    print(f"[SUMMARY]:{passed_count}:{len(test_cases)}")

if __name__ == "__main__":
    sys.path.append('.')
    run_tests()