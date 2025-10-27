const assert = require('assert');
const { ScrabbleScore } = require('./scrablle_score.js'); // Assuming student file

function runTests() {
    const solver = new ScrabbleScore();
    // Test Cases: { word1: string|null, word2: string|null, expected: string }
    const testCases = [
        { word1: "Question?", word2: "Query", expected: "One wins!" },
        { word1: "Apple", word2: "Banana", expected: "Two wins!" },
        { word1: "Programming", word2: "Coding", expected: "One wins!" },
        { word1: "HELLO", word2: "hello", expected: "Tie!" },
        { word1: "CS50", word2: "Harvard", expected: "Two wins!" },
        { word1: "", word2: "Empty", expected: "Two wins!" },
        { word1: "Points!", word2: "Score?", expected: "One wins!" },
        { word1: "Tie", word2: "Tie", expected: "Tie!" },
        { word1: "Test", word2: "", expected: "One wins!" },
        { word1: null, word2: "Word", expected: "Two wins!" },
        { word1: "Word", word2: null, expected: "One wins!" },
        { word1: null, word2: null, expected: "Tie!" }
    ];

    let passedCount = 0;
    let report = [];
    console.log("===== Starting Automated Tests for Scrabble Score Comparator (JavaScript) =====");

    testCases.forEach((tc, i) => {
        let actual = "Error";
        const input1Desc = tc.word1 === null ? "null" : `"${tc.word1}"`;
        const input2Desc = tc.word2 === null ? "null" : `"${tc.word2}"`;
        const caseIdentifier = `Test Case #${i + 1}: Player 1(${input1Desc}) vs Player 2(${input2Desc})`;
        try {
            // Call the updated method
            actual = solver.compareScores(tc.word1, tc.word2);
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