*Myanmar Digit Calculator*

Write a function that takes two Myanmar digit strings (representing non-negative integers) and a character representing an arithmetic operator (+, -, \*, /) as input. The function should perform the calculation and return the result as a Myanmar digit string.

**Rules:**

- Input numbers will be strings containing only Myanmar digits (၀-၉).
- The operator will be one of: '+', '-', '\*', '/'.
- The function should return the calculated result as a string containing only Myanmar digits.
- For division (/), perform integer division (discard any remainder).
- Handle division by zero by returning a specific error string: `"Error: Division by zero"`
- Assume inputs are valid (valid Myanmar digits, valid operator), except for the division by zero case.

*Examples:*

➤ Input: `"၁၂၃"`, `"၄၅၆"`, `'+'` ➔ Output: `"၅၇၉"`
➤ Input: `"၁၀၀"`, `"၁၀"`, `'-'` ➔ Output: `"၉၀"`
➤ Input: `"၂၀"`, `"၅"`, `'*'` ➔ Output: `"၁၀၀"`
➤ Input: `"၂၁"`, `"၅"`, `'/'` ➔ Output: `"၄"` (Integer division)
➤ Input: `"၁၀"`, `"၀"`, `'/'` ➔ Output: `"Error: Division by zero"`

---

*Instructions:*

1. Choose your preferred language (Java/Python/JS).

2. The bot will provide a code template.

3. Implement your logic (including Myanmar digit conversion) *without using external APIs or libraries* for the conversion part. Standard arithmetic operations are allowed.

4. *(Java Specific)*: Do not use `Map` or `HashMap`. Use only basic arrays (`char[]`) for digit mapping.

5. Submit the correct file (e.g., `MyanmarCalculator.java`).
