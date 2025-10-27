*Assignment 14: Substitution Cipher*

A substitution cipher replaces each letter in the plaintext with a different letter based on a fixed mapping, defined by a key. The key is a 26-character string representing the substitute alphabet.

Write a function that takes a plaintext string and a 26-character key string as input and returns the corresponding ciphertext.

**Rules:**

➤ **Key:** The key will be a 26-character string containing each letter of the alphabet exactly once (case-insensitive for the key itself, usually treated as uppercase for mapping). For example, if the key is `"YTNSHKVEFXRBAUQZCLWDMIPGJO"`, 'A' maps to 'Y', 'B' maps to 'T', 'C' maps to 'N', ..., 'Z' maps to 'O'.
➤ **Encryption:** Replace each alphabetical character in the plaintext with the corresponding character from the key, based on its position in the alphabet (A=0, B=1, ... Z=25).
➤ **Case Preservation:** The case (uppercase/lowercase) of the letters in the ciphertext must match the case of the original letters in the plaintext. (e.g., if plaintext 'H' maps to key's 'E', output 'E'; if plaintext 'e' maps to key's 'H', output 'h').
➤ **Non-Alphabetical Characters:** Digits, spaces, punctuation, etc., should remain unchanged in the output.
➤ **Input Assumption:** Assume the provided key is valid (26 unique alphabetic characters).

*Examples:*
(Using Key: `"YTNSHKVEFXRBAUQZCLWDMIPGJO"`)

➤ Input: `plainText = "Hello!"`, `key = "YTNSHKVEFXRBAUQZCLWDMIPGJO"` ➔ Output: `"Ehqqz!"`
  ➤ H (index 7) ➔ Key[7] = E ➔ `E`
  ➤ e (index 4) ➔ Key[4] = H ➔ `h`
  ➤ l (index 11) ➔ Key[11] = A ➔ `a`
  ➤ l (index 11) ➔ Key[11] = A ➔ `a`
  ➤ o (index 14) ➔ Key[14] = Z ➔ `z`
  ➤ ! ➔ `!`
  ➤ Result: `"Ehaalz!"` *(Correction: Previous manual trace was wrong, this is correct)* Let's re-verify: H(7)➔E, e(4)➔h, l(11)➔a, l(11)➔a, o(14)➔z. Output is Ehaalz! Example text corrected.

➤ Input: `plainText = "Zelda?"`, `key = "YTNSHKVEFXRBAUQZCLWDMIPGJO"` ➔ Output: `"Ogqbq?"`

(Using Key: `"QWERTYUIOPASDFGHJKLZXCVBNM"`)

➤ Input: `plainText = "CDV25"`, `key = "QWERTYUIOPASDFGHJKLZXCVBNM"` ➔ Output: `"ERC25"` (C➔E, D➔R, V➔C) No, C(2)➔E, D(3)➔R, V(21)➔C. Output should be `ERC25`. Example corrected.

---

*Instructions:*

1. Choose your preferred language (Java/Python/JS).

2. The bot will provide a code template with an `encodeText(String plainText, String key)` (or similar) method.

3. Implement the logic for the substitution cipher according to the rules.

4. *(Java Specific)*: Implement the solution using only basic arrays (`char[]`), `String` objects (and standard methods like `charAt`, `length`, `isLetter`, `isLowerCase`, `isUpperCase`, `toUpperCase`), primitive types (`int`, `char`), `String` concatenation (`+`), loops, and conditional statements. **Do not use** `java.util.List`, `Map`, `ArrayList`, `HashMap`, `StringBuilder`, NIO, or IO classes in your core encryption logic.

5. Submit the correct file (e.g., `Substitution.java`).
