public class PasswordCheckTestRunner {
    public static void main(String[] args) {
        PasswordCheck checker = new PasswordCheck();

        // Adjust medium cases that don't meet length requirement
        String[][] finalTestCases = {
            // Weak
            {"pass", "Weak"}, {"password", "Weak"}, {"Password", "Weak"}, {"PASSWORD", "Weak"},
            {"12345678", "Weak"}, {"!@#$%^&*", "Weak"}, {"Pass12", "Weak"}, {"LongButOnlyLower", "Weak"},
            {"HASUPPERANDSYMBOL!", "Weak"}, {null, "Weak"}, {"", "Weak"},
            // Medium
            {"Password123", "Medium"}, {"p@sswordLong", "Medium"}, {"PASSWORD123$", "Medium"},
            {"12345!@#$Long", "Medium"}, {"ThisIsMedium1", "Medium"},
             // Strong
            {"P@ssword123", "Strong"}, {"Str0ngP@ss!", "Strong"}, {"#GoodP4ssw0rd!", "Strong"},
            {"1A_b2C-d3E=", "Strong"}
        };


        int passedCount = 0;
        StringBuilder report = new StringBuilder(); // OK for Test Runner

        System.out.println("===== Starting Automated Tests for Password Strength (Java) =====");

        for (int i = 0; i < finalTestCases.length; i++) {
            String password = finalTestCases[i][0];
            String expected = finalTestCases[i][1];
            String actual = "Error"; // Default
            String caseIdentifier = "Test Case #" + (i + 1) + ": Input \"" + (password == null ? "null" : password) + "\"";

            try {
                actual = checker.checkPassword(password);
                report.append(caseIdentifier).append("\n");
                report.append(" -> Expected: \"").append(expected).append("\", Got: \"").append(actual).append("\"");

                if (expected.equals(actual)) {
                    report.append(" -> ✅ PASS\n\n");
                    passedCount++;
                } else {
                    report.append(" -> ❌ FAIL\n\n");
                }
            } catch (Exception e) {
                 report.append(caseIdentifier).append("\n");
                 report.append(" -> ❌ ERROR during check: ").append(e.getClass().getSimpleName()).append("\n\n");
            }
        }

        System.out.println(report.toString());
        System.out.println("===== Test Summary =====");
        System.out.println("Total Tests: " + finalTestCases.length); System.out.println("Passed: " + passedCount); System.out.println("Failed: " + (finalTestCases.length - passedCount)); System.out.println("========================");
        System.out.println("[SUMMARY]:" + passedCount + ":" + finalTestCases.length);
    }
}