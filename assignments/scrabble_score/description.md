*Scrabble Score Comparator*

Scrabble is a word game where players score points by placing tiles, each bearing a single letter, onto a game board. Each letter has an assigned point value.

Write a function that takes **two words** as input, calculates the Scrabble score for each word, and determines which word scores higher.

**Letter Scores:**

➤ (1 point)-A, E, I, L, N, O, R, S, T, U
➤ (2 points)-D, G
➤ (3 points)-B, C, M, P
➤ (4 points)-F, H, V, W, Y
➤ (5 points)-K
➤ (8 points)-J, X
➤ (10 points)-Q, Z

**Rules for Scoring:**

➤ Calculate the score for each word individually.
➤ Scoring is case-insensitive.
➤ Non-letter characters score 0 points.

**Output:**

The function should return one of the following exact strings:

➤ `"One wins!"` if the first word (`wordOne`) scores higher.
➤ `"Two wins!"` if the second word (`wordTwo`) scores higher.
➤ `"Tie!"` if both words score the same.

*Examples:*

➤ Input: `wordOne = "Question?"`, `wordTwo = "Query"` ➔ Output: `"One wins!"` (Score 19 vs 18)
➤ Input: `wordOne = "Apple"`, `wordTwo = "Banana"` ➔ Output: `"Two wins!"` (Score 9 vs 8)
➤ Input: `wordOne = "Tie"`, `wordTwo = "Tie"` ➔ Output: `"Tie!"` (Score 3 vs 3)

---

*Instructions:*

1. Choose your preferred language (Java/Python/JS).

2. The bot will provide a code template with a `compareScores(String wordOne, String wordTwo)` (or similar) method.

3. Implement the logic to calculate the score for *both* words and return the correct comparison result string. You might want a helper function to calculate the score for a single word.

4. *(Java Specific)*: Implement the solution using only basic arrays (`char[]`, `int[]`), `String` objects (and standard methods like `charAt`, `length`, `toLowerCase`/`toUpperCase`), primitive types (`int`), loops, and conditional statements. **Do not use** `java.util.List`, `Map`, `ArrayList`, `HashMap`, `StringBuilder`, NIO, or IO classes in your core scoring logic.

5. Submit the correct file (e.g., `ScrabbleScore.java`).
