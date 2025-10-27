public class CaesarCipherTestRunner {
    public static void main(String[] args) {
        CaesarCipher cipher = new CaesarCipher();

        // Test Cases: [plainText, key, expectedCipherText]
        Object[][] testCases = {
            {"Hello, World!", 1, "Ifmmp, Xpsme!"},
            {"xyz", 3, "abc"},
            {"XYZ", 3, "ABC"},
            {"Be sure to drink your Ovaltine!", 13, "Or fher gb qevax lbhe Binygvar!"},
            {"Ciphering.", 26, "Ciphering."},
            {"middle-Outz", 2, "okffng-Qwvb"},
            {"A", 0, "A"},
            {"Z", 1, "A"},
            {"a", 25, "z"},
            {"123 ABC xyz .,!", 5, "123 FGH cde .,!"},
            {"", 10, ""}, // Empty string test
            {"Test", 52, "Test"} // Key is multiple of 26
        };

        int passedCount = 0;
        StringBuilder report = new StringBuilder(); // StringBuilder is OK for Test Runner output

        System.out.println("===== Starting Automated Tests for Caesar Cipher (Java) =====");

        for (int i = 0; i < testCases.length; i++) {
            String plainText = (String) testCases[i][0];
            int key = (int) testCases[i][1];
            String expected = (String) testCases[i][2];
            String actual = "Error"; // Default
            String caseIdentifier = "Test Case #" + (i + 1) + ": Input \"" + plainText + "\", Key=" + key;

            try {
                actual = cipher.encodeText(plainText, key);
                report.append(caseIdentifier).append("\n");
                report.append(" -> Expected: \"").append(expected).append("\"\n");
                report.append(" ->      Got: \"").append(actual).append("\"");

                if (expected.equals(actual)) {
                    report.append(" -> ✅ PASS\n\n");
                    passedCount++;
                } else {
                    report.append(" -> ❌ FAIL\n\n");
                }
            } catch (Exception e) {
                 report.append(caseIdentifier).append("\n");
                 report.append(" -> ❌ ERROR during encryption: ").append(e.getClass().getSimpleName()).append("\n\n");
            }
        }

        System.out.println(report.toString());
        System.out.println("===== Test Summary =====");
        System.out.println("Total Tests: " + testCases.length); System.out.println("Passed: " + passedCount); System.out.println("Failed: " + (testCases.length - passedCount)); System.out.println("========================");
        System.out.println("[SUMMARY]:" + passedCount + ":" + testCases.length);
    }
}