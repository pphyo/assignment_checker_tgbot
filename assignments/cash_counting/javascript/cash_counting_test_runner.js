const assert = require('assert');
const { CashCounting } = require('./cash_counting.js'); // Assuming student file is Cash.js

function runTests() {
    const solver = new CashCounting();
    // Corrected Test Cases: { amount: number, expected: number }
    const testCases = [
        { amount: 70, expected: 3 }, { amount: 63, expected: 5 }, { amount: 47, expected: 5 },
        { amount: 268, expected: 6 }, { amount: 10000, expected: 1 }, { amount: 15, expected: 1 },
        { amount: 14, expected: 5 }, { amount: 29, expected: 6 }, { amount: 0, expected: 0 },
        { amount: 1, expected: 1 }, { amount: 4, expected: 4 }, { amount: 5, expected: 1 },
        { amount: 9, expected: 5 }, { amount: 10, expected: 1 }, { amount: 12345, expected: 8 }
    ];

    let passedCount = 0;
    let report = [];
    console.log("===== Starting Automated Tests for Cash Change (JavaScript) =====");

    testCases.forEach((tc, i) => {
        let actual = -1;
        const caseIdentifier = `Test Case #${i + 1}: Input amount=${tc.amount}`;
        try {
            actual = solver.calculateNotes(tc.amount);
            assert.strictEqual(actual, tc.expected);
            report.push(`${caseIdentifier} -> ✅ PASS`);
            passedCount++;
        } catch (error) {
             report.push(`${caseIdentifier} -> ❌ FAIL/ERROR: Expected ${tc.expected}, but got ${actual}`);
        }
    });

    console.log(report.join('\n\n'));
    console.log("\n===== Test Summary =====");
    console.log(`Total Tests: ${testCases.length}`); console.log(`Passed: ${passedCount}`); console.log(`Failed: ${testCases.length - passedCount}`); console.log("========================");
    console.log(`[SUMMARY]:${passedCount}:${testCases.length}`);
}

runTests();