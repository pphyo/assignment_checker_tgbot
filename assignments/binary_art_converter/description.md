*Text to Binary Art*

Write a function that takes a string as input and converts it into a visual representation using binary patterns.

**Conversion Steps:**

1. Get the ASCII value for each character in the input string.
2. Convert each ASCII value into its 8-bit binary string representation (ensure leading zeros if the binary is shorter than 8 bits).
3. For each 8-bit binary string:
    ➤ Replace every '0' with the black circle emoji ('\u26ab', ⚫).
    ➤ Replace every '1' with the white circle emoji ('\u26aa', ⚪).
4. Each character's resulting emoji string should be on a new line.
5. The final output should be a single string containing all the emoji lines, separated by newline characters (`\n`).

*Example:*

➤ Input: `"Hi"`
➤ Output:

```bash
⚫⚪⚫⚫⚪⚫⚫⚫
⚫⚪⚪⚫⚪⚫⚫⚪
```

*(Explanation: 'H' is ASCII 72 ➔ binary 01001000 ➔ ⚫⚪⚫⚫⚪⚫⚫⚫, 'i' is ASCII 105 ➔ binary 01101001 ➔ ⚫⚪⚪⚫⚪⚫⚫⚪)*

➤ Input: `"A"`
➤ Output: `⚫⚪⚫⚫⚫⚫⚫⚪`

*(Explanation: 'A' is ASCII 65 ➔ binary 01000001 ➔ ⚫⚪⚫⚫⚫⚫⚫⚪)*

➤ Input: `"Hello"`
➤ Output:

```bash
⚫⚪⚫⚫⚪⚫⚫⚫
⚫⚪⚪⚫⚫⚪⚫⚪
⚫⚪⚪⚫⚪⚪⚫⚫
⚫⚪⚪⚫⚪⚪⚫⚫
⚫⚪⚪⚫⚪⚪⚪⚪
```

---

*Instructions:*

1. Choose your preferred language (Java/Python/JS).

2. The bot will provide a code template.

3. Implement your logic following the conversion steps.

4. *(Java Specific)*: Implement the solution using only basic arrays (`char[]`) and `StringBuilder`. Do not use `java.util.List`, `java.util.Map`, or other Collections Framework classes. Standard String methods like `getBytes`, `Integer.toBinaryString`, `String.format` are allowed.

5. Submit the correct file (e.g., `BinaryArtConverter.java`).
