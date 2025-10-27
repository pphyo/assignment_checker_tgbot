*Credit Card Validator*

Most credit cards use Luhn's algorithm to check if the card number is potentially valid (syntactically). Additionally, card numbers follow patterns regarding their length and starting digits to identify the card network (e.g., AMEX, MASTERCARD, VISA).

Write a function that takes a credit card number (as a string) and determines if it's valid according to Luhn's algorithm and, if so, which network it belongs to.

**Luhn's Algorithm:**

1. Starting from the second-to-last digit, multiply every other digit by 2.
2. If any product is a two-digit number (e.g., 6 \* 2 = 12), add the _digits_ of the product together (1 + 2 = 3).
3. Sum up all the digits obtained from step 2.
4. Sum up all the digits that *were not* multiplied by 2 in step 1.
5. Add the results from step 3 and step 4 together.
6. If the total sum ends in 0 (i.e., `total % 10 == 0`), the number is potentially valid according to the algorithm.

**Card Network Rules:**

➤ **AMEX:** Starts with `34` or `37`; Length: 15 digits.
➤ **MASTERCARD:** Starts with `51`, `52`, `53`, `54`, or `55`; Length: 16 digits.
➤ **VISA:** Starts with `4`; Length: 13 or 16 digits.

**Output:**
Return one of the following strings: `"AMEX"`, `"MASTERCARD"`, `"VISA"`, or `"INVALID"`. A number is `"INVALID"` if it fails Luhn's algorithm OR if it passes Luhn's but doesn't match any known network's starting digits and length rules.

*Examples:*

➤ Input: `"4062901840127322"` (VISA, Valid Luhn) ➔ Output: `"VISA"`
➤ Input: `"378282246310005"` (AMEX, Valid Luhn) ➔ Output: `"AMEX"`
➤ Input: `"5105105105105100"` (MASTERCARD, Valid Luhn) ➔ Output: `"MASTERCARD"`
➤ Input: `"4062901840127321"` (VISA prefix, Invalid Luhn) ➔ Output: `"INVALID"`
➤ Input: `"1234567890123"` (Invalid prefix/length) ➔ Output: `"INVALID"`

---

*Instructions:*

1. Choose your preferred language (Java/Python/JS).

2. The bot will provide a code template.

3. Implement Luhn's algorithm and the card network checks. Treat the input number as a **String**.

4. *(Java Specific)*: Implement the solution using only basic arrays (`char[]`), `String` objects (and their standard methods like `charAt`, `length`, `startsWith`, `substring`), primitive types (`int`, `long`), `StringBuilder`, loops, and conditional statements. **Do not use** `java.util.List`, `java.util.Map`, `java.util.ArrayList`, `java.util.HashMap`, NIO, or IO classes in your core validation logic.

5. Submit the correct file (e.g., `Credit.java`).
