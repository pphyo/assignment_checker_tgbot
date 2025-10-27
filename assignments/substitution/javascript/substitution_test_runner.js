const assert = require('assert');
const { Substitution } = require('./substitution.js'); // Assuming student file

function runTests() {
    const solver = new Substitution();
    // Test Cases: { plain: string, key: string, expected: string }
    const key1 = "ZYXWVUTSRQPONMLKJIHGFEDCBA";
    const key2 = "YTNSHKVEFXRBAUQZCLWDMIPGJO";
    const key3 = "QWERTYUIOPASDFGHJKLZXCVBNM";
    const testCases = [
        { plain: "Hello, World!", key: key1, expected: "Svool, Dliow!" },
        { plain: "Programming is fun!", key: key1, expected: "Kiltiznnrmt rh ufm!" },
        { plain: "Testing 1 2 3", key: key1, expected: "Gvhgrmt 1 2 3" },
        { plain: "abcdefghijklmnopqrstuvwxyz", key: key1, expected: "zyxwvutsrqponmlkjihgfedcba" },
        { plain: "ABCDEFGHIJKLMNOPQRSTUVWXYZ", key: key1, expected: "ZYXWVUTSRQPONMLKJIHGFEDCBA" },
        { plain: "Hello!", key: key2, expected: "Ehaalz!" }, // Corrected expected
        { plain: "Zelda?", key: key2, expected: "Ogqbq?" },
        { plain: "Caesar Cipher", key: key2, expected: "Nrgbry Nvcuor" },
        { plain: "CS50", key: key3, expected: "EB50" }, // Corrected expected
        { plain: "", key: key1, expected: "" },
        { plain: "No Change", key: "ABCDEFGHIJKLMNOPQRSTUVWXYZ", expected: "No Change" }
    ];

    let passedCount = 0;
    let report = [];
    console.log("===== Starting Automated Tests for Substitution Cipher (JavaScript) =====");

    testCases.forEach((tc, i) => {
        let actual = "Error";
        const caseIdentifier = `Test Case #${i + 1}: Input "${tc.plain}", Key="${tc.key.substring(0,5)}..."`;
        try {
            actual = solver.encodeText(tc.plain, tc.key);
            assert.strictEqual(actual, tc.expected);
            report.push(`${caseIdentifier} -> ✅ PASS`);
            passedCount++;
        } catch (error) {
             report.push(`${caseIdentifier} -> ❌ FAIL/ERROR: Expected "${tc.expected}", but got "${actual}"`);
        }
        report.push(''); // Add blank line
    });

    console.log(report.join('\n'));
    console.log("===== Test Summary =====");
    console.log(`Total Tests: ${testCases.length}`); console.log(`Passed: ${passedCount}`); console.log(`Failed: ${testCases.length - passedCount}`); console.log("========================");
    console.log(`[SUMMARY]:${passedCount}:${testCases.length}`);
}

runTests();