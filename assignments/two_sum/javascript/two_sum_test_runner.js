const assert = require('assert');
const { TwoSum } = require('./TwoSum.js');

function runTests() {
    const solver = new TwoSum();
    const testCases = [
        { nums: [2, 7, 11, 15], target: 9, expected: [0, 1] },
        { nums: [3, 2, 4], target: 6, expected: [1, 2] },
        { nums: [3, 3], target: 6, expected: [0, 1] },
    ];

    let passedCount = 0;
    let report = [];
    console.log("===== Starting Automated Tests for TwoSum (JavaScript) =====");

    testCases.forEach((tc, i) => {
        let actual, expected;
        try {
            actual = solver.solve(tc.nums, tc.target);
            expected = tc.expected;

            actual.sort((a, b) => a - b);
            expected.sort((a, b) => a - b);

            assert.deepStrictEqual(actual, expected);
            report.push(`Test Case #${i + 1}: Input nums=${JSON.stringify(tc.nums)}, target=${tc.target} -> ✅ PASS`);
            passedCount++;
        } catch (error) {
            report.push(`Test Case #${i + 1}: Input nums=${JSON.stringify(tc.nums)}, target=${tc.target} -> ❌ FAIL/ERROR: Expected ${JSON.stringify(expected)}, but got ${JSON.stringify(actual)}`);
        }
    });

    console.log(report.join('\n\n'));
    console.log("\n===== Test Summary =====");
    console.log(`Total Tests: ${testCases.length}`); console.log(`Passed: ${passedCount}`); console.log(`Failed: ${testCases.length - passedCount}`); console.log("========================");
    console.log(`[SUMMARY]:${passedCount}:${testCases.length}`);
}

runTests();