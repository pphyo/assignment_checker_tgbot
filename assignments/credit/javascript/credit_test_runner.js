const assert = require('assert');
const { Credit } = require('./credit.js'); // Assuming student file is Credit.js

function runTests() {
    const solver = new Credit();
    // Test Cases: { number: string|null, expected: string }
    const testCases = [
        { number: "4062901840127322", expected: "VISA" }, { number: "4000000000000", expected: "VISA" },
        { number: "378282246310005", expected: "AMEX" }, { number: "340000000000000", expected: "AMEX" },
        { number: "5105105105105100", expected: "MASTERCARD" }, { number: "5555555555555555", expected: "MASTERCARD" },
        { number: "4062901840127321", expected: "INVALID" }, { number: "378282246310006", expected: "INVALID" },
        { number: "5105105105105101", expected: "INVALID" }, { number: "411122223333", expected: "INVALID" },
        { number: "41112222333344445", expected: "INVALID" }, { number: "6011000000000000", expected: "INVALID" },
        { number: "1234567890123", expected: "INVALID" }, { number: null, expected: "INVALID" },
        { number: "", expected: "INVALID" }, { number: "abcde12345abcde", expected: "INVALID" }
    ];

    let passedCount = 0;
    let report = [];
    console.log("===== Starting Automated Tests for Credit Card Validator (JavaScript) =====");

    testCases.forEach((tc, i) => {
        let actual = "Error";
        const inputDesc = tc.number === null ? "null" : `"${tc.number}"`;
        const caseIdentifier = `Test Case #${i + 1}: Input ${inputDesc}`;
        try {
            actual = solver.validateCreditCard(tc.number);
            assert.strictEqual(actual, tc.expected);
            report.push(`${caseIdentifier} -> ✅ PASS`);
            passedCount++;
        } catch (error) {
             report.push(`${caseIdentifier} -> ❌ FAIL/ERROR: Expected "${tc.expected}", but got "${actual}"`);
        }
    });

    console.log(report.join('\n\n'));
    console.log("\n===== Test Summary =====");
    console.log(`Total Tests: ${testCases.length}`); console.log(`Passed: ${passedCount}`); console.log(`Failed: ${testCases.length - passedCount}`); console.log("========================");
    console.log(`[SUMMARY]:${passedCount}:${testCases.length}`);
}

runTests();