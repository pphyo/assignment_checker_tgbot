*Caesar Cipher*

The Caesar cipher is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. This fixed number is called the key.

Write a function that takes a plaintext string and an integer key as input and returns the corresponding ciphertext.

**Rules:**

➤ Only rotate alphabetical characters (a-z, A-Z).
➤ Preserve the case of the letters (e.g., 'H' shifted by 3 becomes 'K', 'e' shifted by 3 becomes 'h').
➤ Non\-alphabetical characters (digits, spaces, punctuation) should remain unchanged in the output.
➤ The rotation should "wrap around" the alphabet (e.g., 'z' shifted by 1 becomes 'a', 'Y' shifted by 3 becomes 'B').
➤ The key (`k`) will be a non-negative integer.

*Examples:*

➤ Input: `plainText = "Hello, World!"`, `key = 1` ➔ Output: `"Ifmmp, Xpsme!"`
➤ Input: `plainText = "xyz"` , `key = 3` ➔ Output: `"abc"`
➤ Input: `plainText = "Be sure to drink your Ovaltine!"`, `key = 13` ➔ Output: `"Or fher gb qevax lbhe Binygvar!"`
➤ Input: `plainText = "Ciphering."`, `key = 26` ➔ Output: `"Ciphering."` (Key 26 means no shift)
➤ Input: `plainText = "middle-Outz"`, `key = 2` ➔ Output: `"okffng-Qwvb"`

---

*Instructions:*

1. Choose your preferred language (Java/Python/JS).

2. The bot will provide a code template with an `encodeText(String plainText, int key)` (or similar) method.

3. Implement the logic for the Caesar cipher according to the rules.

4. _(Java Specific)_: Implement the solution using only basic arrays (`char[]`), `String` objects (and standard methods like `charAt`, `length`, `isLetter`, `isLowerCase`, `isUpperCase`), primitive types (`int`, `char`), `String` concatenation (`+`), loops, and conditional statements. **Do not use** `java.util.List`, `Map`, `ArrayList`, `HashMap`, `StringBuilder`, NIO, or IO classes in your core encryption logic.

5. Submit the correct file (e.g., `CaesarCipher.java`).
