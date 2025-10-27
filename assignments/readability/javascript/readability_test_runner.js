const assert = require('assert');
const { Readability } = require('./readability.js'); // Assuming student file

function runTests() {
    const solver = new Readability();
    // Test Cases: { text: string, expected: string }
    const testCases = [
        { text: "One fish. Two fish. Red fish. Blue fish.", expected: "Before Grade 1" },
        { text: "Would you like them here or there? I would not like them here or there. I would not like them anywhere.", expected: "Grade 2" },
        { text: "Congratulations! Today is your day. You're off to Great Places! You're off and away!", expected: "Grade 3" },
        { text: "Harry Potter was a highly unusual boy in many ways. For one thing, he hated the summer holidays more than any other time of year. For another, he really wanted to do his homework, but was forced to do it in secret, in the dead of the night. And he also happened to be a wizard.", expected: "Grade 5" },
        { text: "A large phone book enables you to call anybody. The reason is that it contains the numbers of everybody.", expected: "Grade 9" },
        { text: "It was a bright cold day in April, and the clocks were striking thirteen. Winston Smith, his chin nuzzled into his breast in an effort to escape the vile wind, slipped quickly through the glass doors of Victory Mansions, though not quickly enough to prevent a swirl of gritty dust from entering along with him.", expected: "Grade 8" },
        { text: "Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, 'and what is the use of a book,' thought Alice 'without pictures or conversation?'", expected: "Grade 8" },
        { text: "There are more things in Heaven and Earth, Horatio, than are dreamt of in your philosophy.", expected: "Grade 9" },
        { text: "It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife.", expected: "Grade 12" },
        { text: "A beginning is the time for taking the most delicate care that balances are correct.", expected: "Grade 11" },
        { text: "", expected: "Before Grade 1" },
        { text: "One.", expected: "Before Grade 1" },
        { text: "aaaaaaaaaa.", expected: "Before Grade 1" },
        { text: "a a a. a a a? a a a!", expected: "Before Grade 1" },
        { text: "This sentence is grade sixteen plus.", expected: "Grade 16+" }
    ];


    let passedCount = 0;
    let report = [];
    console.log("===== Starting Automated Tests for Readability (JavaScript) =====");

    testCases.forEach((tc, i) => {
        let actual = "Error";
        const caseIdentifier = `Test Case #${i + 1}: Input "${tc.text.substring(0, 20)}..."`;
        try {
            actual = solver.checkText(tc.text);
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