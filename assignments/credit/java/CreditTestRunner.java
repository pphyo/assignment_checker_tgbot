public class CreditTestRunner {
    public static void main(String[] args) {
        Credit validator = new Credit();

        // Test Cases: [cardNumber, expectedResult]
        String[][] testCases = {
            // Valid VISA
            {"4062901840127322", "VISA"},      // 16 digits
            {"4000000000000", "VISA"},         // 13 digits (Example valid Luhn)
            // Valid AMEX
            {"378282246310005", "AMEX"},      // 15 digits
            {"340000000000000", "AMEX"},      // 15 digits (Example valid Luhn)
             // Valid MASTERCARD
            {"5105105105105100", "MASTERCARD"},// 16 digits
            {"5555555555555555", "MASTERCARD"},// 16 digits (Example valid Luhn)
            // Invalid Luhn
            {"4062901840127321", "INVALID"}, // VISA prefix, bad checksum
            {"378282246310006", "INVALID"}, // AMEX prefix, bad checksum
            {"5105105105105101", "INVALID"}, // MC prefix, bad checksum
            // Invalid Length
            {"411122223333", "INVALID"},       // 12 digits
            {"41112222333344445", "INVALID"}, // 17 digits
            // Invalid Prefix
            {"6011000000000000", "INVALID"}, // Valid Luhn, unknown prefix (Discover)
            {"1234567890123", "INVALID"},     // 13 digits, wrong prefix
             // Edge cases
            {null, "INVALID"},                 // Null input
            {"", "INVALID"},                   // Empty string
            {"abcde12345abcde", "INVALID"}     // Non-digits
        };

        int passedCount = 0;
        StringBuilder report = new StringBuilder();
        System.out.println("===== Starting Automated Tests for Credit Card Validator (Java) =====");

        for (int i = 0; i < testCases.length; i++) {
            String input = testCases[i][0];
            String expected = testCases[i][1];
            String actual = "Error"; // Default
            String caseIdentifier = "Test Case #" + (i + 1) + ": Input \"" + (input == null ? "null" : input) + "\"";

            try {
                actual = validator.validateCreditCard(input);
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
                 report.append(" -> ❌ ERROR: ").append(e.getClass().getSimpleName()).append("\n\n");
            }
        }

        System.out.println(report.toString());
        System.out.println("===== Test Summary =====");
        System.out.println("Total Tests: " + testCases.length); System.out.println("Passed: " + passedCount); System.out.println("Failed: " + (testCases.length - passedCount)); System.out.println("========================");
        System.out.println("[SUMMARY]:" + passedCount + ":" + testCases.length);
    }
}