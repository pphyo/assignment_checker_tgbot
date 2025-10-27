public class CashCountingTestRunner {
    public static void main(String[] args) {
        CashCounting calculator = new CashCounting();

         // Corrected Test Cases
         int[][] correctedTestCases = {
            {70, 3},   // 50(1) + 15(1) + 5(1)
            {63, 5},   // 50(1) + 10(1) + 1(3)
            {47, 5},   // 15(3) + 1(2)
            {268, 6},  // 200(1) + 50(1) + 15(1) + 1(3)
            {10000, 1},// 10000(1)
            {15, 1},   // 15(1)
            {14, 5},   // 10(1) + 1(4)
            {29, 6},   // 15(1) + 10(1) + 1(4)
            {0, 0},
            {1, 1},
            {4, 4},    // 1(4)
            {5, 1},
            {9, 5},    // 5(1) + 1(4)
            {10, 1},
            {12345, 8} // 10000(1) + 1000(2) + 200(1) + 100(1) + 15(3)
        };


        int passedCount = 0;
        StringBuilder report = new StringBuilder();

        System.out.println("===== Starting Automated Tests for Cash Change (Java) =====");

        for (int i = 0; i < correctedTestCases.length; i++) {
            int inputAmount = correctedTestCases[i][0];
            int expected = correctedTestCases[i][1];
            int actual = -1; // Default to an invalid value
            String caseIdentifier = "Test Case #" + (i + 1) + ": Input amount=" + inputAmount;

            try {
                actual = calculator.calculateNotes(inputAmount);
                report.append(caseIdentifier).append("\n");
                report.append(" -> Expected: ").append(expected).append(", Got: ").append(actual);

                if (actual == expected) {
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
        System.out.println("Total Tests: " + correctedTestCases.length); System.out.println("Passed: " + passedCount); System.out.println("Failed: " + (correctedTestCases.length - passedCount)); System.out.println("========================");
        System.out.println("[SUMMARY]:" + passedCount + ":" + correctedTestCases.length);
    }
}