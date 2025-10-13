import java.util.Arrays;

public class TwoSumTestRunner {
    public static void main(String[] args) {
        TwoSum twoSumSolver = new TwoSum();

        // Test Case များ
        int[][] numsInputs = {
            {2, 7, 11, 15},
            {3, 2, 4},
            {3, 3}
        };
        int[] targetInputs = {9, 6, 6};
        int[][] expectedOutputs = {
            {0, 1},
            {1, 2},
            {0, 1}
        };

        int passedCount = 0;
        StringBuilder report = new StringBuilder();

        System.out.println("===== Starting Automated Tests for TwoSum =====");

        for (int i = 0; i < numsInputs.length; i++) {
            try {
                int[] actualOutput = twoSumSolver.solve(numsInputs[i], targetInputs[i]);

                Arrays.sort(actualOutput);
                Arrays.sort(expectedOutputs[i]);

                report.append("Test Case #").append(i + 1)
                      .append(": Input nums=").append(Arrays.toString(numsInputs[i]))
                      .append(", target=").append(targetInputs[i]).append("\n");

                report.append(" -> Expected: ").append(Arrays.toString(expectedOutputs[i]))
                      .append(", Got: ").append(Arrays.toString(actualOutput));

                if (Arrays.equals(actualOutput, expectedOutputs[i])) {
                    report.append(" -> ✅ PASS\n\n");
                    passedCount++;
                } else {
                    report.append(" -> ❌ FAIL\n\n");
                }
            } catch (Exception e) {
                report.append("Test Case #").append(i + 1)
                      .append(": Input nums=").append(Arrays.toString(numsInputs[i]))
                      .append(", target=").append(targetInputs[i]).append("\n");
                report.append(" -> ❌ ERROR: ").append(e.getClass().getSimpleName()).append("\n\n");
            }
        }

        System.out.println(report.toString());
        System.out.println("===== Test Summary =====");
        System.out.println("Total Tests: " + numsInputs.length);
        System.out.println("Passed: " + passedCount);
        System.out.println("Failed: " + (numsInputs.length - passedCount));
        System.out.println("========================");
        System.out.println("[SUMMARY]:" + passedCount + ":" + numsInputs.length);
    }
}