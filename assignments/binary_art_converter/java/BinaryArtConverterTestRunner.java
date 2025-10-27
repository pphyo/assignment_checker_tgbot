public class BinaryArtConverterTestRunner {
    public static void main(String[] args) {
        BinaryArtConverter converter = new BinaryArtConverter();

        // Test Cases: [input_string, expected_output_string]
        String[][] testCases = {
            {"Hi",
             """
               ⚫⚪⚫⚫⚪⚫⚫⚫
               ⚫⚪⚪⚫⚪⚫⚫⚪"""},    // i (105) = 01101001
            {"A",
             "⚫⚪⚫⚫⚫⚫⚫⚪"},    // A (65) = 01000001
            {"z",
              "⚫⚪⚪⚪⚪⚫⚪⚫"},   // z (122) = 01111010
            {"", ""},           // Empty string
            {"1",               // Digit '1' (ASCII 49)
              "⚫⚫⚪⚪⚫⚫⚫⚪"}, // 49 = 00110001
            { "Hello",
              """
              ⚫⚪⚫⚫⚪⚫⚫⚫
              ⚫⚪⚪⚫⚫⚪⚫⚪
              ⚫⚪⚪⚫⚪⚪⚫⚫
              ⚫⚪⚪⚫⚪⚪⚫⚫
              ⚫⚪⚪⚫⚪⚪⚪⚪"""
             }
        };

        int passedCount = 0;
        StringBuilder report = new StringBuilder();

        System.out.println("===== Starting Automated Tests for BinaryArtConverter (Java) =====");

        for (int i = 0; i < testCases.length; i++) {
            String input = testCases[i][0];
            String expected = testCases[i][1];
            String actual = "";
            String caseIdentifier = "Test Case #" + (i + 1) + ": Input \"" + input + "\"";

            try {
                actual = converter.convertToBinaryArt(input);
                report.append(caseIdentifier).append("\n");
                // Compare strings, ensuring proper handling of newlines
                if (expected.equals(actual)) {
                    report.append(" -> Expected:\n").append(expected).append("\n");
                    report.append(" ->      Got:\n").append(actual).append("\n");
                    report.append(" -> ✅ PASS\n\n");
                    passedCount++;
                } else {
                    report.append(" -> Expected:\n").append(expected).append("\n");
                    report.append(" ->      Got:\n").append(actual).append("\n");
                    report.append(" -> ❌ FAIL\n\n");
                }
            } catch (Exception e) {
                 report.append(caseIdentifier).append("\n");
                 report.append(" -> ❌ ERROR: ").append(e.getClass().getSimpleName()).append("\n\n");
            }
        }

        System.out.println(report.toString());
        System.out.println("===== Test Summary =====");
        System.out.println("Total Tests: " + testCases.length); System.out.println("Passed: " + passedCount); System.out.println("Failed: " + (testCases.length - passedCount)); System.out.println("========================");
        System.out.println("[SUMMARY]:" + passedCount + ":" + testCases.length);
    }
}