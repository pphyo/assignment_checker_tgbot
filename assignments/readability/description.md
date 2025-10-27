*Readability (Coleman-Liau Index)*

The Coleman-Liau index is a readability test designed to estimate the U.S. grade level required to understand a piece of text. It's calculated using the following formula:

**`index = 0.0588 * L - 0.296 * S - 15.8`**

Where:

➤ `L` is the average number of letters per 100 words in the text.
➤ `S` is the average number of sentences per 100 words in the text.

Write a function that takes a string of text as input and outputs the estimated grade level based on the Coleman-Liau index.

**Rules for Calculation:**

1. **Letters:** Count any uppercase or lowercase letter (A-Z, a-z).
2. **Words:** Count any sequence of characters separated by spaces. Assume sentences do not start or end with spaces, and there's only one space between words. The number of words is the number of spaces + 1 (unless the text is empty).
3. **Sentences:** Count any occurrence of a period (`.`), exclamation point (`!`), or question mark (`?`) as the end of a sentence.
4. **Calculate L and S:**
    ➤ `L = (total letters / total words) * 100`
    ➤ `S = (total sentences / total words) * 100`
    ➤ *(Handle division by zero if there are no words)*
5. **Calculate Index:** Apply the formula using the calculated `L` and `S`.
6. **Determine Output:**
    ➤ If the calculated index is less than 1, return the string `"Before Grade 1"`.
    ➤ If the calculated index is 16 or greater, return the string `"Grade 16+"`.
    ➤ Otherwise, round the index to the nearest whole number and return the string `"Grade X"`, where `X` is the rounded index (e.g., `"Grade 5"`, `"Grade 10"`).

*Examples:*

➤ Input: `"One fish. Two fish. Red fish. Blue fish."` ➔ Output: `"Before Grade 1"`
➤ Input: `"Would you like them here or there? I would not like them here or there. I would not like them anywhere."` ➤ Output: `"Grade 2"`
➤ Input: `"Congratulations! Today is your day. You're off to Great Places! You're off and away!"` ➔ Output: `"Grad➤ 3"`
➤ Input: `"A large phone book enables you to call anybody. The reason is that it contains the numbers of every➤ody."` ➔ Output: `"Grade 9"`

---

*Instructions:*

1. Choose your preferred language (Java/Python/JS).

2. The bot will provide a code template with a `checkText(String text)` (or similar) method.

3. Implement the logic to count letters, words, and sentences, calculate the index, and determine the grade level string.

4. *(Java Specific)*: Implement the solution using only basic arrays (`char[]`), `String` objects (and standard methods like `charAt`, `length`, `isLetter`, `isWhitespace`), primitive types (`int`, `float`/`double`), `String` concatenation (`+`), `Math.round()`, loops, and conditional statements. **Do not use** `java.util.List`, `Map`, `ArrayList`, `HashMap`, `StringBuilder`, NIO, or IO classes in your core calculation logic.

5. Submit the correct file (e.g., `Readability.java`).
