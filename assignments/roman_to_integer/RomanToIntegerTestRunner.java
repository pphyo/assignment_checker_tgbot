public class RomanToIntegerTestRunner {

    public static void main(String[] args) {
        RomanToInteger converter = new RomanToInteger();

        String[] inputs = {"III", "LVIII", "MCMXCIV", "IX", "IV", "CM"};
        int[] expectedOutputs = {3, 58, 1994, 9, 4, 900};

        int passedCount = 0;
        StringBuilder report = new StringBuilder();

        System.out.println("===== Starting Automated Tests for RomanToInteger =====");

        for (int i = 0; i < inputs.length; i++) {
            try {
                int actualOutput = converter.convert(inputs[i]);

                report.append("Test Case #").append(i + 1).append(": Input '").append(inputs[i]).append("'\n");
                report.append(" -> Expected: ").append(expectedOutputs[i]).append(", Got: ").append(actualOutput);

                if (actualOutput == expectedOutputs[i]) {
                    report.append(" -> ✅ PASS\n\n");
                    passedCount++;
                } else {
                    report.append(" -> ❌ FAIL\n\n");
                }
            } catch (Exception e) {
                report.append("Test Case #").append(i + 1).append(": Input '").append(inputs[i]).append("'\n");
                report.append(" -> ❌ ERROR: ").append(e.getMessage()).append("\n\n");
            }
        }

        System.out.println(report.toString());
        System.out.println("===== Test Summary =====");
        System.out.println("Total Tests: " + inputs.length);
        System.out.println("Passed: " + passedCount);
        System.out.println("Failed: " + (inputs.length - passedCount));
        System.out.println("========================");

        System.out.println("[SUMMARY]:" + passedCount + ":" + inputs.length);
    }
}