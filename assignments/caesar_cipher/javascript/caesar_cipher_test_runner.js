const assert = require('assert');
const { CaesarCipher } = require('./caesar_cipher.js'); // Assuming student file

function runTests() {
    const solver = new CaesarCipher();
    // Test Cases: { plain: string, key: number, expected: string }
    const testCases = [
        { plain: "Hello, World!", key: 1, expected: "Ifmmp, Xpsme!" },
        { plain: "xyz", key: 3, expected: "abc" }, { plain: "XYZ", key: 3, expected: "ABC" },
        { plain: "Be sure to drink your Ovaltine!", key: 13, expected: "Or fher gb qevax lbhe Binygvar!" },
        { plain: "Ciphering.", key: 26, expected: "Ciphering." }, { plain: "middle-Outz", key: 2, expected: "okffng-Qwvb" },
        { plain: "A", key: 0, expected: "A" }, { plain: "Z", key: 1, expected: "A" }, { plain: "a", key: 25, expected: "z" },
        { plain: "123 ABC xyz .,!", key: 5, expected: "123 FGH cde .,!" }, { plain: "", key: 10, expected: "" },
        { plain: "Test", key: 52, expected: "Test" }
    ];

    let passedCount = 0;
    let report = [];
    console.log("===== Starting Automated Tests for Caesar Cipher (JavaScript) =====");

    testCases.forEach((tc, i) => {
        let actual = "Error";
        const caseIdentifier = `Test Case #${i + 1}: Input "${tc.plain}", Key=${tc.key}`;
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