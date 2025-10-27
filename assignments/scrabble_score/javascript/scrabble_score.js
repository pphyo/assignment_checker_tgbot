class ScrabbleScore {
    /**
     * Compares the Scrabble scores of two words.
     * @param {string} wordOne The first word.
     * @param {string} wordTwo The second word.
     * @returns {"One wins!"|"Two wins!"|"Tie!"}
     */
    compareScores(wordOne, wordTwo) {
        // TODO: Implement scoring logic for both words and compare.
        // You might want a helper method to compute the score for one word.
        return "Tie!"; // Placeholder
    }

    // Optional: Helper method to compute score for one word
    _computeScore(word) {
      // TODO: Implement scoring for a single word here
      return 0;
    }
}

module.exports = { ScrabbleScore };