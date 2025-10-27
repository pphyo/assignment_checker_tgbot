const assert = require('assert');
const { EnglishDigitToMyanmarDigit } = require('./EnglishDigitToMyanmarDigit.js');

function runTests() {
    const solver = new EnglishDigitToMyanmarDigit();
    const testCases = [
        { input: 0, expected: "၀" }, { input: 9, expected: "၉" },
        { input: 10, expected: "၁၀" }, { input: 11, expected: "၁၁" },
        { input: 1234, expected: "၁၂၃၄" }, { input: 2314, expected: "၂၃၁၄" },
        { input: 987654321, expected: "၉၈၇၆၅၄၃၂၁" }
    ];

    let passedCount = 0;
    let report = [];
    console.log("===== Starting Automated Tests for EnglishDigitToMyanmarDigit (JavaScript) =====");

    testCases.forEach((tc, i) => {
        let actual = "";
        try {
            actual = solver.convert(tc.input);
            assert.strictEqual(actual, tc.expected);
            report.push(`Test Case #${i + 1}: Input ${tc.input} -> ✅ PASS`);
            passedCount++;
        } catch (error) {
             report.push(`Test Case #${i + 1}: Input ${tc.input} -> ❌ FAIL/ERROR: Expected "${tc.expected}", but got "${actual}"`);
        }
    });

    console.log(report.join('\n\n'));
    console.log("\n===== Test Summary =====");
    console.log(`Total Tests: ${testCases.length}`); console.log(`Passed: ${passedCount}`); console.log(`Failed: ${testCases.length - passedCount}`); console.log("========================");
    console.log(`[SUMMARY]:${passedCount}:${testCases.length}`);
}

runTests();