import sys
from substitution import Substitution # Import the student's class

def run_tests():
    solver = Substitution()
    # Test Cases: (plainText, key, expectedCipherText)
    key1 = "ZYXWVUTSRQPONMLKJIHGFEDCBA"
    key2 = "YTNSHKVEFXRBAUQZCLWDMIPGJO"
    key3 = "QWERTYUIOPASDFGHJKLZXCVBNM"
    test_cases = [
        ("Hello, World!", key1, "Svool, Dliow!"),
        ("Programming is fun!", key1, "Kiltiznnrmt rh ufm!"),
        ("Testing 1 2 3", key1, "Gvhgrmt 1 2 3"),
        ("abcdefghijklmnopqrstuvwxyz", key1, "zyxwvutsrqponmlkjihgfedcba"),
        ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", key1, "ZYXWVUTSRQPONMLKJIHGFEDCBA"),
        ("Hello!", key2, "Ehaalz!"), # Corrected expected
        ("Zelda?", key2, "Ogqbq?"),
        ("Caesar Cipher", key2, "Nrgbry Nvcuor"),
        ("CS50", key3, "EB50"), # Corrected expected
        ("", key1, ""),
        ("No Change", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "No Change")
    ]
    passed_count = 0
    report = []
    print("===== Starting Automated Tests for Substitution Cipher (Python) =====")

    for i, (plain_text, key, expected) in enumerate(test_cases):
        actual = "Error"
        case_identifier = f'Test Case #{i + 1}: Input "{plain_text}", Key="{key[:5]}..."'
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