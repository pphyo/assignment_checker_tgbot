// runner.js
const assert = require('assert');
const { RomanToInteger } = require('./roman_to_integer.js'); // Assumes student file exports the class

function runTests() {
    const solver = new RomanToInteger();
    const testCases = [
        { input: "III", expected: 3 },
        { input: "LVIII", expected: 58 },
        { input: "MCMXCIV", expected: 1994 },
    ];

    let passedCount = 0;
    let report = [];
    console.log("===== Starting Automated Tests for RomanToInteger (JavaScript) =====");

    testCases.forEach((tc, i) => {
        try {
            const actual = solver.convert(tc.input);
            assert.strictEqual(actual, tc.expected, `Expected ${tc.expected}, but got ${actual}`);
            report.push(`Test Case #${i + 1}: Input '${tc.input}' -> ✅ PASS`);
            passedCount++;
        } catch (error) {
            report.push(`Test Case #${i + 1}: Input '${tc.input}' -> ❌ FAIL/ERROR: ${error.message}`);
        }
    });

    console.log(report.join('\n\n'));
    console.log("\n===== Test Summary =====");
    console.log(`Total Tests: ${testCases.length}`);
    console.log(`Passed: ${passedCount}`);
    console.log(`Failed: ${testCases.length - passedCount}`);
    console.log("========================");

    console.log(`[SUMMARY]:${passedCount}:${testCases.length}`);
}

runTests();