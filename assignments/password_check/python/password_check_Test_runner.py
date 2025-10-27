import sys
from password_check import PasswordCheck # Import the student's class

def run_tests():
    solver = PasswordCheck()
    # Test Cases: (password, expectedStrength)
    test_cases = [
        # Weak
        ("pass", "Weak"), ("password", "Weak"), ("Password", "Weak"), ("PASSWORD", "Weak"),
        ("12345678", "Weak"), ("!@#$%^&*", "Weak"), ("Pass12", "Weak"), ("LongButOnlyLower", "Weak"),
        ("HASUPPERANDSYMBOL!", "Weak"), (None, "Weak"), ("", "Weak"),
        # Medium
        ("Password123", "Medium"), ("p@sswordLongEnough", "Medium"), ("PASSWORD123$", "Medium"),
        ("12345!@#$LongEnough", "Medium"), ("ThisIsMedium1", "Medium"),
         # Strong
        ("P@ssword123", "Strong"), ("Str0ngP@ss!", "Strong"), ("#GoodP4ssw0rd!", "Strong"),
        ("1A_b2C-d3E=", "Strong")
    ]
    passed_count = 0
    report = []
    print("===== Starting Automated Tests for Password Strength (Python) =====")

    for i, (password, expected) in enumerate(test_cases):
        actual = "Error"
        input_desc = "None" if password is None else f'"{password}"'
        case_identifier = f'Test Case #{i + 1}: Input {input_desc}'
        try:
            actual = solver.check_password(password)
            report.append(case_identifier)
            report.append(f' -> Expected: "{expected}", Got: "{actual}"')

            if actual == expected:
                report.append(" -> ✅ PASS\n")
                passed_count += 1
            else:
                report.append(" -> ❌ FAIL\n")
        except Exception as e:
            report.append(case_identifier)
            report.append(f" -> ❌ ERROR during check: {type(e).__name__}\n")

    print("\n".join(report))
    print("===== Test Summary ====="); print(f"Total Tests: {len(test_cases)}"); print(f"Passed: {passed_count}"); print(f"Failed: {len(test_cases) - passed_count}"); print("========================")
    print(f"[SUMMARY]:{passed_count}:{len(test_cases)}")

if __name__ == "__main__":
    sys.path.append('.')
    run_tests()