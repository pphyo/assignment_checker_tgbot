const assert = require('assert');
const { IntegerToRoman } = require('./IntegerToRoman.js');

function runTests() {
    const solver = new IntegerToRoman();
    const testCases = [
        { input: 3, expected: "III" }, { input: 4, expected: "IV" }, { input: 9, expected: "IX" },
        { input: 58, expected: "LVIII" }, { input: 1994, expected: "MCMXCIV" }, { input: 3749, expected: "MMMDCCXLIX" }
    ];

    let passedCount = 0;
    let report = [];
    console.log("===== Starting Automated Tests for IntegerToRoman (JavaScript) =====");

    testCases.forEach((tc, i) => {
        try {
            const actual = solver.convert(tc.input);
            assert.strictEqual(actual, tc.expected);
            report.push(`Test Case #${i + 1}: Input ${tc.input} -> ✅ PASS`);
            passedCount++;
        } catch (error) {
            report.push(`Test Case #${i + 1}: Input ${tc.input} -> ❌ FAIL/ERROR: Expected "${tc.expected}", but got "${error.actual}"`);
        }
    });

    console.log(report.join('\n\n'));
    console.log("\n===== Test Summary =====");
    console.log(`Total Tests: ${testCases.length}`); console.log(`Passed: ${passedCount}`); console.log(`Failed: ${testCases.length - passedCount}`); console.log("========================");
    console.log(`[SUMMARY]:${passedCount}:${testCases.length}`);
}

runTests();