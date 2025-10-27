const assert = require('assert');
const { MyanmarDigitCalculator } = require('./MyanmarCalculator.js');

function runTests() {
    const solver = new MyanmarDigitCalculator();
    const testCases = [
        { n1: "၁၂၃", n2: "၄၅၆", op: '+', expected: "၅၇၉" },
        { n1: "၁၀၀", n2: "၁၀", op: '-', expected: "၉၀" },
        { n1: "၂၀", n2: "၅", op: '*', expected: "၁၀၀" },
        { n1: "၂၁", n2: "၅", op: '/', expected: "၄" },
        { n1: "၁၀", n2: "၀", op: '/', expected: "Error: Division by zero" },
        { n1: "၀", n2: "၅", op: '+', expected: "၅" },
        { n1: "၅", n2: "၀", op: '*', expected: "၀" },
        { n1: "၉၈၇", n2: "၁၂၃", op: '+', expected: "၁၁၁၀" },
        { n1: "၁၀", n2: "၂၀", op: '-', expected: "-၁၀" }, // Test negative result
    ];

    let passedCount = 0;
    let report = [];
    console.log("===== Starting Automated Tests for MyanmarCalculator (JavaScript) =====");

    testCases.forEach((tc, i) => {
        let actual = "";
        try {
            actual = solver.calculate(tc.n1, tc.n2, tc.op);
            assert.strictEqual(actual, tc.expected);
            report.push(`Test Case #${i + 1}: Input '${tc.n1}' ${tc.op} '${tc.n2}' -> ✅ PASS`);
            passedCount++;
        } catch (error) {
             report.push(`Test Case #${i + 1}: Input '${tc.n1}' ${tc.op} '${tc.n2}' -> ❌ FAIL/ERROR: Expected "${tc.expected}", but got "${actual}"`);
        }
    });

    console.log(report.join('\n\n'));
    console.log("\n===== Test Summary =====");
    console.log(`Total Tests: ${testCases.length}`); console.log(`Passed: ${passedCount}`); console.log(`Failed: ${testCases.length - passedCount}`); console.log("========================");
    console.log(`[SUMMARY]:${passedCount}:${testCases.length}`);
}

runTests();