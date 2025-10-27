public class ReadabilityTestRunner {
    public static void main(String[] args) {
        Readability checker = new Readability();

        // Test Cases: [inputText, expectedGradeString]
        String[][] testCases = {
            {"One fish. Two fish. Red fish. Blue fish.", "Before Grade 1"},
            {"Would you like them here or there? I would not like them here or there. I would not like them anywhere.", "Grade 2"},
            {"Congratulations! Today is your day. You're off to Great Places! You're off and away!", "Grade 3"},
            {"Harry Potter was a highly unusual boy in many ways. For one thing, he hated the summer holidays more than any other time of year. For another, he really wanted to do his homework, but was forced to do it in secret, in the dead of the night. And he also happened to be a wizard.", "Grade 5"},
            {"A large phone book enables you to call anybody. The reason is that it contains the numbers of everybody.", "Grade 9"},
            {"It was a bright cold day in April, and the clocks were striking thirteen. Winston Smith, his chin nuzzled into his breast in an effort to escape the vile wind, slipped quickly through the glass doors of Victory Mansions, though not quickly enough to prevent a swirl of gritty dust from entering along with him.", "Grade 8"},
            {"Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, 'and what is the use of a book,' thought Alice 'without pictures or conversation?'", "Grade 8"},
            {"There are more things in Heaven and Earth, Horatio, than are dreamt of in your philosophy.", "Grade 9"},
            {"It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife.", "Grade 12"},
             {"A beginning is the time for taking the most delicate care that balances are correct.", "Grade 11"}, // Example near Grade 11/12
            {"", "Before Grade 1"}, // Empty string
            {"One.", "Before Grade 1"}, // Very simple
            {"aaaaaaaaaa.", "Before Grade 1"}, // Many letters, few words/sentences
            {"a a a. a a a? a a a!", "Before Grade 1"}, // Many words/sentences, few letters
            {"This sentence is grade sixteen plus.", "Grade 16+"} // Example designed to be high
        };

        int passedCount = 0;
        StringBuilder report = new StringBuilder(); // OK for Test Runner

        System.out.println("===== Starting Automated Tests for Readability (Java) =====");

        for (int i = 0; i < testCases.length; i++) {
            String inputText = testCases[i][0];
            String expected = testCases[i][1];
            String actual = "Error"; // Default
            String caseIdentifier = "Test Case #" + (i + 1) + ": Input \"" + inputText.substring(0, Math.min(inputText.length(), 20)) + "...\"";

            try {
                actual = checker.checkText(inputText);
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
                 report.append(" -> ❌ ERROR during calculation: ").append(e.getClass().getSimpleName()).append("\n\n");
            }
        }

        System.out.println(report.toString());
        System.out.println("===== Test Summary =====");
        System.out.println("Total Tests: " + testCases.length); System.out.println("Passed: " + passedCount); System.out.println("Failed: " + (testCases.length - passedCount)); System.out.println("========================");
        System.out.println("[SUMMARY]:" + passedCount + ":" + testCases.length);
    }
}