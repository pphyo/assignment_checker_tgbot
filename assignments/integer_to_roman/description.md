*Integer to Roman*

[Image of Roman numerals on an ancient stone tablet]

Seven different symbols represent Roman numerals with the following values:

| Symbol | Value |
| :---: | :---: |
| I | 1 |
| V | 5 |
| X | 10 |
| L | 50 |
| C | 100 |
| D | 500 |
| M | 1000 |

Given an integer, convert it to a Roman numeral. Roman numerals are formed by converting decimal place values from highest to lowest.

**Rules:**

1. If a value does not start with 4 or 9, append the maximal value symbol and subtract its value from the remainder.
2. If a value starts with 4 or 9, use the subtractive form:
    ➤ `IV` (4), `IX` (9)
    ➤ `XL` (40), `XC` (90)
    ➤ `CD` (400), `CM` (900)
3. Powers of 10 (`I`, `X`, `C`, `M`) can be appended consecutively at most 3 times.

**Examples:**

➤ Input: `num = 3749` ➔ Output: `"MMMDCCXLIX"`
➤ Input: `num = 58` ➔ Output: `"LVIII"`
➤ Input: `num = 1994` ➔ Output: `"MCMXCIV"`

---

*Instructions:*

1. Choose your preferred language.

2. The bot will provide a code template.

3. Implement your logic and submit the correct file.
