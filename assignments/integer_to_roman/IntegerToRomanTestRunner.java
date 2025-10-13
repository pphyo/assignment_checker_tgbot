public class IntegerToRomanTestRunner {
    public static void main(String[] args) {
        IntegerToRoman converter = new IntegerToRoman();

        // Test Cases
        int[] inputs = {3, 4, 9, 58, 1994, 3749, 3999};
        String[] expectedOutputs = {"III", "IV", "IX", "LVIII", "MCMXCIV", "MMMDCCXLIX", "MMMCMXCIX"};

        int passedCount = 0;
        StringBuilder report = new StringBuilder();

        System.out.println("===== Starting Automated Tests for IntegerToRoman =====");

        for (int i = 0; i < inputs.length; i++) {
            try {
                String actualOutput = converter.convert(inputs[i]);

                report.append("Test Case #").append(i + 1).append(": Input '").append(inputs[i]).append("'\n");
                report.append(" -> Expected: \"").append(expectedOutputs[i]).append("\", Got: \"").append(actualOutput).append("\"");

                if (expectedOutputs[i].equals(actualOutput)) {
                    report.append(" -> ✅ PASS\n\n");
                    passedCount++;
                } else {
                    report.append(" -> ❌ FAIL\n\n");
                }
            } catch (Exception e) {
                report.append("Test Case #").append(i + 1).append(": Input '").append(inputs[i]).append("'\n");
                report.append(" -> ❌ ERROR: ").append(e.getClass().getSimpleName()).append(" - ").append(e.getMessage()).append("\n\n");
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