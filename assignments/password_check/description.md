*Password Strength Checker*

Write a function that checks the strength of a given password based on a set of criteria and returns "Weak", "Medium", or "Strong".

**Password Strength Criteria:**
A password's strength is determined by meeting the following requirements:

1. **Length:** Must be at least 8 characters long.
2. **Uppercase:** Must contain at least one uppercase letter (A-Z).
3. **Lowercase:** Must contain at least one lowercase letter (a-z).
4. **Digit:** Must contain at least one digit (0-9).
5. **Symbol:** Must contain at least one symbol from the following set: `!@#$%^&*()_+-=[]{};':"\\|,.<>/?~`

**Strength Levels:**

➤ **Weak:** Fails the length requirement (less than 8 characters) OR meets the length requirement but satisfies only 1 or 2 of the other criteria (Uppercase, Lowercase, Digit, Symbol).
➤ **Medium:** Meets the length requirement AND satisfies exactly 3 of the other criteria.
➤ **Strong:** Meets the length requirement AND satisfies all 4 of the other criteria.

**Output:**
The function should return one of the following exact strings: `"Weak"`, `"Medium"`, or `"Strong"`.

*Examples:*

➤ Input: `"password"` ➔ Output: `"Weak"` (Meets length, has Lowercase, but missing Upper, Digit, Symbol)
➤ Input: `"Password"` ➔ Output: `"Weak"` (Meets length, has Upper, Lower, but missing Digit, Symbol)
➤ Input: `"Password123"` ➔ Output: `"Medium"` (Meets length, has Upper, Lower, Digit, but missing Symbol)
➤ Input: `"P@ssword123"` ➔ Output: `"Strong"` (Meets length, has all criteria)
➤ Input: `"short"` ➔ Output: `"Weak"` (Fails length requirement)
➤ Input: `"ALLCAPS"` ➔ Output: `"Weak"` (Fails length, missing Lower, Digit, Symbol)
➤ Input: `"12345678"` ➔ Output: `"Weak"` (Meets length, has Digit, but missing Upper, Lower, Symbol)
➤ Input: `"Symbols#@!"` ➔ Output: `"Medium"` (Meets length, has Upper, Lower, Symbol, but missing Digit)

---

*Instructions:*

1. Choose your preferred language (Java/Python/JS).

2. The bot will provide a code template with a `checkPassword(String password)` (or similar) method.

3. Implement the logic to check all criteria and determine the strength level.

4. *(Java Specific)*: Implement the solution using only basic arrays (`char[]`), `String` objects (and standard methods like `charAt`, `length`, `isLetter`, `isDigit`, `isUpperCase`, `isLowerCase`), primitive types (`boolean`, `int`, `char`), `String` concatenation (`+`), loops, and conditional statements. **Do not use** `java.util.List`, `Map`, `ArrayList`, `HashMap`, `StringBuilder`, NIO, or IO classes in your core checking logic. A simple string containing allowed symbols is permitted.

5. Submit the correct file (e.g., `PasswordCheck.java`).
