public class NumberToMyanmarWordTestRunner {

    // Helper function to normalize "တစ်" to "တ" before major units for comparison
    private static String normalizePrefix(String word) {
        return word.replace("တစ်ဆယ်", "တဆယ်")
                   .replace("တစ်ရာ", "တရာ")
                   .replace("တစ်ထောင်", "တထောင်")
                   .replace("တစ်သောင်း", "တသောင်း")
                   .replace("တစ်သိန်း", "တသိန်း")
                   .replace("တစ်သန်း", "တသန်း")
                   .replace("တစ်ကုဋေ", "တကုဋေ");
    }


    public static void main(String[] args) {
        NumberToMyanmarWord converter = new NumberToMyanmarWord();

        int[] inputs = {0, 5, 10, 11, 25, 100, 101, 110, 1000, 1001, 1234, 10000, 10101, 11000, 110101, 123456, 1000000};
        // Expected outputs use simplified grammar AND the "တ" prefix for consistency in the test itself
        String[] expectedOutputs = {
            "သုညကျပ်", "ငါးကျပ်", "တဆယ်ကျပ်", "တဆယ့်တစ်ကျပ်", "နှစ်ဆယ့်ငါးကျပ်", "တရာကျပ်", "တရာတစ်ကျပ်", "တရာတဆယ်ကျပ်",
            "တထောင်ကျပ်", "တထောင်တစ်ကျပ်", "တထောင်နှစ်ရာသုံးဆယ့်လေးကျပ်",
            "တသောင်းကျပ်", "တသောင်းတရာတကျပ်", "တသောင်းတထောင်ကျပ်",
            "တသိန်းတသောင်းတရာတကျပ်", "တသိန်းနှစ်သောင်းသုံးထောင်လေးရာငါးဆယ့်ခြောက်ကျပ်",
            "တသန်းကျပ်"
        };


        int passedCount = 0;
        StringBuilder report = new StringBuilder();
        System.out.println("===== Starting Automated Tests for NumberToMyanmarWord (Java) =====");

        for (int i = 0; i < inputs.length; i++) {
            String expected = expectedOutputs[i];
            String actual = "";
            try {
                actual = converter.convert(inputs[i]);
                report.append("Test Case #").append(i + 1).append(": Input '").append(inputs[i]).append("'\n");
                report.append(" -> Expected: \"").append(expected).append("\", Got: \"").append(actual).append("\"");

                // Normalize both before comparing
                String normalizedExpected = normalizePrefix(expected);
                String normalizedActual = normalizePrefix(actual);

                if (normalizedExpected.equals(normalizedActual)) {
                    report.append(" -> ✅ PASS\n\n");
                    passedCount++;
                } else {
                    report.append(" -> ❌ FAIL (Normalized: Expected '").append(normalizedExpected).append("', Got '").append(normalizedActual).append("')\n\n");
                }
            } catch (Exception e) {
                 report.append(" -> ❌ ERROR: ").append(e.getClass().getSimpleName()).append("\n\n");
            }
        }
        // ... (Rest of the runner code: print report, summary, [SUMMARY] line) ...
        System.out.println(report.toString());
        System.out.println("===== Test Summary =====");
        System.out.println("Total Tests: " + inputs.length); System.out.println("Passed: " + passedCount); System.out.println("Failed: " + (inputs.length - passedCount)); System.out.println("========================");
        System.out.println("[SUMMARY]:" + passedCount + ":" + inputs.length);
    }
}