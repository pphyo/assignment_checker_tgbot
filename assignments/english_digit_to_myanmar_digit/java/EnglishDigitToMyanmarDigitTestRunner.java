public class EnglishDigitToMyanmarDigitTestRunner {
    public static void main(String[] args) {
        EnglishDigitToMyanmarDigit converter = new EnglishDigitToMyanmarDigit();

        int[] inputs = {0, 9, 10, 11, 1234, 2314, 987654321};
        String[] expectedOutputs = {"၀", "၉", "၁၀", "၁၁", "၁၂၃၄", "၂၃၁၄", "၉၈၇၆၅၄၃၂၁"};

        int passedCount = 0;
        StringBuilder report = new StringBuilder();

        System.out.println("===== Starting Automated Tests for EnglishDigitToMyanmarDigit (Java) =====");

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
                 report.append(" -> ❌ ERROR: ").append(e.getClass().getSimpleName()).append("\n\n");
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