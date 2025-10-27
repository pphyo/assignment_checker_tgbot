public class MyanmarDigitCalculatorTestRunner {
    public static void main(String[] args) {
        MyanmarDigitCalculator calculator = new MyanmarDigitCalculator();

        // Test Cases: [numStr1, numStr2, operator, expectedOutput]
        String[][] testCases = {
            {"၁၂၃", "၄၅၆", "+", "၅၇၉"},
            {"၁၀၀", "၁၀", "-", "၉၀"},
            {"၂၀", "၅", "*", "၁၀၀"},
            {"၂၁", "၅", "/", "၄"},
            {"၁၀", "၀", "/", "Error: Division by zero"},
            {"၀", "၅", "+", "၅"},
            {"၅", "၀", "*", "၀"},
            {"၉၈၇", "၁၂၃", "+", "၁၁၁၀"}, // Test carry-over
            {"၁၀", "၂၀", "-", "-၁၀"} // Test negative result
        };

        int passedCount = 0;
        StringBuilder report = new StringBuilder();

        System.out.println("===== Starting Automated Tests for MyanmarCalculator (Java) =====");

        for (int i = 0; i < testCases.length; i++) {
            String numStr1 = testCases[i][0];
            String numStr2 = testCases[i][1];
            char operator = testCases[i][2].charAt(0); // Get char from string
            String expected = testCases[i][3];
            String actual = "";

            try {
                actual = calculator.calculate(numStr1, numStr2, operator);
                report.append("Test Case #").append(i + 1).append(": Input '")
                      .append(numStr1).append("' ").append(operator).append(" '").append(numStr2).append("'\n");
                report.append(" -> Expected: \"").append(expected).append("\", Got: \"").append(actual).append("\"");

                if (expected.equals(actual)) {
                    report.append(" -> ✅ PASS\n\n");
                    passedCount++;
                } else {
                    report.append(" -> ❌ FAIL\n\n");
                }
            } catch (Exception e) {
                report.append("Test Case #").append(i + 1).append(": Input '")
                      .append(numStr1).append("' ").append(operator).append(" '").append(numStr2).append("'\n");
                report.append(" -> ❌ ERROR: ").append(e.getClass().getSimpleName()).append("\n\n");
            }
        }

        System.out.println(report.toString());
        System.out.println("===== Test Summary =====");
        System.out.println("Total Tests: " + testCases.length); System.out.println("Passed: " + passedCount); System.out.println("Failed: " + (testCases.length - passedCount)); System.out.println("========================");
        System.out.println("[SUMMARY]:" + passedCount + ":" + testCases.length);
    }
}