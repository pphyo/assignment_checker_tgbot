public class ScrabbleScoreTestRunner {
    public static void main(String[] args) {
        ScrabbleScore comparator = new ScrabbleScore(); // Changed variable name

        // Test Cases: [word1, word2, expectedResultString]
        String[][] testCases = {
            {"Question?", "Query", "One wins!"},
            {"Apple", "Banana", "Two wins!"},
            {"Programming", "Coding", "One wins!"},
            {"HELLO", "hello", "Tie!"},
            {"CS50", "Harvard", "Two wins!"},
            {"", "Empty", "Two wins!"},
            {"Points!", "Score?", "One wins!"},
            {"Tie", "Tie", "Tie!"},
            {"Test", "", "One wins!"}, // Test with empty string
            {null, "Word", "Two wins!"}, // Test with null (should score 0)
            {"Word", null, "One wins!"},
            {null, null, "Tie!"}
        };

        int passedCount = 0;
        StringBuilder report = new StringBuilder();

        System.out.println("===== Starting Automated Tests for Scrabble Score Comparator (Java) =====");

        for (int i = 0; i < testCases.length; i++) {
            String word1 = testCases[i][0];
            String word2 = testCases[i][1];
            String expected = testCases[i][2];
            String actual = "Error"; // Default
            String caseIdentifier = "Test Case #" + (i + 1) + ": Player 1(\"" + (word1 == null ? "null" : word1)
                                   + "\") vs Player 2(\"" + (word2 == null ? "null" : word2) + "\")";

            try {
                // Call the updated method
                actual = comparator.compareScores(word1, word2);

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
                 report.append(" -> ❌ ERROR during comparison: ").append(e.getClass().getSimpleName()).append("\n\n");
            }
        }

        System.out.println(report.toString());
        System.out.println("===== Test Summary =====");
        System.out.println("Total Tests: " + testCases.length); System.out.println("Passed: " + passedCount); System.out.println("Failed: " + (testCases.length - passedCount)); System.out.println("========================");
        System.out.println("[SUMMARY]:" + passedCount + ":" + testCases.length);
    }
}