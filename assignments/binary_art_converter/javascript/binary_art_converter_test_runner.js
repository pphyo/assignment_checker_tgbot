const assert = require('assert');
const { BinaryArtConverter } = require('./binary_art_converter.js'); // Assuming student file

function runTests() {
    const solver = new BinaryArtConverter();
    const testCases = [
        { input: "Hi", expected: "⚫⚪⚫⚫⚪⚫⚫⚫\n⚫⚪⚪⚫⚫⚪⚫⚪" },
        { input: "A", expected: "⚫⚪⚫⚫⚫⚫⚫⚪" },
        { input: "z", expected: "⚫⚪⚪⚪⚪⚫⚪⚫" },
        { input: "", expected: "" },
        { input: "1", expected: "⚫⚫⚪⚪⚫⚫⚫⚪" },
        { input: "Hello", expected: "⚫⚪⚫⚫⚪⚫⚫⚫\n⚫⚪⚪⚫⚫⚪⚫⚪\n⚫⚪⚪⚫⚪⚪⚫⚫\n⚫⚪⚪⚫⚪⚪⚫⚫\n⚫⚪⚪⚫⚪⚪⚪⚪" }
    ];

    let passedCount = 0;
    let report = [];
    console.log("===== Starting Automated Tests for BinaryArtConverter (JavaScript) =====");

    testCases.forEach((tc, i) => {
        let actual = "";
        const caseIdentifier = `Test Case #${i + 1}: Input "${tc.input}"`;
        try {
            actual = solver.convertToBinaryArt(tc.input);
            // Use strictEqual for exact string comparison including newlines
            assert.strictEqual(actual, tc.expected);
            report.push(`${caseIdentifier} -> ✅ PASS`);
            passedCount++;
        } catch (error) {
             // Show expected vs actual clearly on failure
             report.push(`${caseIdentifier} -> ❌ FAIL/ERROR:\n -> Expected:\n${tc.expected}\n ->      Got:\n${actual}`);
        }
    });

    console.log(report.join('\n\n'));
    console.log("\n===== Test Summary =====");
    console.log(`Total Tests: ${testCases.length}`); console.log(`Passed: ${passedCount}`); console.log(`Failed: ${testCases.length - passedCount}`); console.log("========================");
    console.log(`[SUMMARY]:${passedCount}:${testCases.length}`);
}

runTests();