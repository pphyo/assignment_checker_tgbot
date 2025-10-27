public class SubstitutionTestRunner {
    public static void main(String[] args) {
        Substitution cipher = new Substitution();

        // Test Cases: [plainText, key, expectedCipherText]
        // Key 1: Standard Alphabet Reversed
        String key1 = "ZYXWVUTSRQPONMLKJIHGFEDCBA";
        // Key 2: CS50 Example Key
        String key2 = "YTNSHKVEFXRBAUQZCLWDMIPGJO";
         // Key 3: Another Example Key
        String key3 = "QWERTYUIOPASDFGHJKLZXCVBNM";


        String[][] testCases = {
            {"Hello, World!", key1, "Svool, Dliow!"},
            {"Programming is fun!", key1, "Kiltiznnrmt rh ufm!"},
            {"Testing 1 2 3", key1, "Gvhgrmt 1 2 3"},
            {"abcdefghijklmnopqrstuvwxyz", key1, "zyxwvutsrqponmlkjihgfedcba"},
            {"ABCDEFGHIJKLMNOPQRSTUVWXYZ", key1, "ZYXWVUTSRQPONMLKJIHGFEDCBA"},
            {"Hello!", key2, "Ehaalz!"}, // Corrected expected output
            {"Zelda?", key2, "Ogqbq?"},
            {"Caesar Cipher", key2, "Nrgbry Nvcuor"},
            {"CS50", key3, "EB50"}, // Corrected expected output
            {"", key1, ""}, // Empty string
            {"No Change", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "No Change"} // Identity key
        };

        int passedCount = 0;
        StringBuilder report = new StringBuilder(); // OK for Test Runner

        System.out.println("===== Starting Automated Tests for Substitution Cipher (Java) =====");

        for (int i = 0; i < testCases.length; i++) {
            String plainText = testCases[i][0];
            String key = testCases[i][1];
            String expected = testCases[i][2];
            String actual = "Error"; // Default
            String caseIdentifier = "Test Case #" + (i + 1) + ": Input \"" + plainText + "\", Key=\""+ key.substring(0,5)+"...\"";

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