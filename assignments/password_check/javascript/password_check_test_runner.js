const assert = require('assert');
const { PasswordCheck } = require('./password_check.js'); // Assuming student file

function runTests() {
    const solver = new PasswordCheck();
    // Test Cases: { password: string|null, expected: string }
    const testCases = [
        // Weak
        { password: "pass", expected: "Weak" }, { password: "password", expected: "Weak" },
        { password: "Password", expected: "Weak" }, { password: "PASSWORD", expected: "Weak" },
        { password: "12345678", expected: "Weak" }, { password: "!@#$%^&*", expected: "Weak" },
        { password: "Pass12", expected: "Weak" }, { password: "LongButOnlyLower", expected: "Weak" },
        { password: "HASUPPERANDSYMBOL!", expected: "Weak" }, { password: null, expected: "Weak" },
        { password: "", expected: "Weak" },
        // Medium
        { password: "Password123", expected: "Medium" }, { password: "p@sswordLongEnough", expected: "Medium" },
        { password: "PASSWORD123$", expected: "Medium" }, { password: "12345!@#$LongEnough", expected: "Medium" },
        { password: "ThisIsMedium1", expected: "Medium" },
         // Strong
        { password: "P@ssword123", expected: "Strong" }, { password: "Str0ngP@ss!", expected: "Strong" },
        { password: "#GoodP4ssw0rd!", expected: "Strong" }, { password: "1A_b2C-d3E=", expected: "Strong" }
    ];

    let passedCount = 0;
    let report = [];
    console.log("===== Starting Automated Tests for Password Strength (JavaScript) =====");

    testCases.forEach((tc, i) => {
        let actual = "Error";
        const inputDesc = tc.password === null ? "null" : `"${tc.password}"`;
        const caseIdentifier = `Test Case #${i + 1}: Input ${inputDesc}`;
        try {
            actual = solver.checkPassword(tc.password);
            assert.strictEqual(actual, tc.expected);
            report.push(`${caseIdentifier} -> ✅ PASS (Result: "${actual}")`);
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