const assert = require('assert');
const { NumberToMyanmarWord } = require('./NumberToMyanmarWord.js');

// Helper function to normalize "တစ်" to "တ" before major units
function normalizePrefix(word) {
    // Use regex for efficient replacement
    return word.replace(/တစ်(ဆယ်|ရာ|ထောင်|သောင်း|သိန်း|သန်း|ကုဋေ)/g, 'တ$1');
}


function runTests() {
    const solver = new NumberToMyanmarWord();
    // Expected outputs use simplified grammar AND the "တ" prefix
    const testCases = [
        { input: 0, expected: "သုညကျပ်" }, { input: 5, expected: "ငါးကျပ်" },
        { input: 10, expected: "တဆယ်ကျပ်" }, { input: 11, expected: "တဆယ့်တစ်ကျပ်" },
        { input: 25, expected: "နှစ်ဆယ့်ငါးကျပ်" }, { input: 100, expected: "တရာကျပ်" },
        { input: 101, expected: "တရာတစ်ကျပ်" }, { input: 110, expected: "တရာတဆယ်ကျပ်" },
        { input: 1000, expected: "တထောင်ကျပ်" }, { input: 1001, expected: "တထောင်တစ်ကျပ်" },
        { input: 1234, expected: "တထောင်နှစ်ရာသုံးဆယ့်လေးကျပ်" }, { input: 10000, expected: "တသောင်းကျပ်" },
        { input: 10101, expected: "တသောင်းတရာတကျပ်" }, { input: 11000, expected: "တသောင်းတထောင်ကျပ်" },
        { input: 110101, expected: "တသိန်းတသောင်းတရာတကျပ်" },
        { input: 123456, expected: "တသိန်းနှစ်သောင်းသုံးထောင်လေးရာငါးဆယ့်ခြောက်ကျပ်" },
        { input: 1000000, expected: "တသန်းကျပ်" }
    ];

    let passedCount = 0;
    let report = [];
    console.log("===== Starting Automated Tests for NumberToMyanmarWord (JavaScript) =====");

    testCases.forEach((tc, i) => {
        let actual = "";
        let normalizedExpected = "";
        let normalizedActual = "";
        try {
            actual = solver.convert(tc.input);

            // Normalize both before comparing
            normalizedExpected = normalizePrefix(tc.expected);
            normalizedActual = normalizePrefix(actual);

            assert.strictEqual(normalizedActual, normalizedExpected);
            report.push(`Test Case #${i + 1}: Input ${tc.input} -> ✅ PASS (Got: "${actual}")`);
            passedCount++;
        } catch (error) {
             report.push(`Test Case #${i + 1}: Input ${tc.input} -> ❌ FAIL/ERROR: Expected "${tc.expected}", Got "${actual}" (Normalized: Expected '${normalizedExpected}', Got '${normalizedActual}')`);
        }
    });

    // ... (Rest of the runner code: print report, summary, [SUMMARY] line) ...
    console.log(report.join('\n\n'));
    console.log("\n===== Test Summary =====");
    console.log(`Total Tests: ${testCases.length}`); console.log(`Passed: ${passedCount}`); console.log(`Failed: ${testCases.length - passedCount}`); console.log("========================");
    console.log(`[SUMMARY]:${passedCount}:${testCases.length}`);
}

runTests();