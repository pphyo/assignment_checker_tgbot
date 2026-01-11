*Myanmar Cash Change Counter*

Myanmar currency has the following banknotes in circulation (Kyat): 10000, 5000, 1000, 500, 200, 100, 50, 15, 10, 5, 1.

Write a function that takes a non-negative integer amount (representing Kyat) and calculates the *minimum* total number of banknotes required to make up that amount using the available denominations.

**Rules:**

➤ Use the greedy approach: always use as many of the largest possible denomination first.
➤ The 15 Kyat note is included in the available denominations.
➤ Return only the total count of banknotes used.

*Examples:*

➤ Input: `70` ➔ Output: `3` (Explanation: 1 x 50 Ks + 1 x 15 Ks + 1 x 5 Ks) *Correction: Example output adjusted based on greedy approach* (1x50 + 1x10 + 1x10 is 3 notes too, but greedy uses 1x50, 1x15, 1x5 = 3 notes) *Let's recalculate the provided examples with greedy:*
  ➤ Input `70`: 1x50 (rem 20) ➔ 1x15 (rem 5) ➔ 1x5 (rem 0) = **3 notes**
  ➤ Input `63`: 1x50 (rem 13) ➔ 0x15 ➔ 1x10 (rem 3) ➔ 0x5 ➔ 3x1 (rem 0) = **5 notes**
  ➤ Input `47`: 0x50 ➔ 3x15 (rem 2) ➔ 0x10 ➔ 0x5 ➔ 2x1 (rem 0) = **5 notes** *(Your example output 6 seems incorrect with a greedy approach)*
➤ Input: `268` ➔ Output: `6` (1x200 + 1x50 + 1x15 + 0x10 + 0x5 + 3x1)
➤ Input: `0` ➔ Output: `0`

---

*Instructions:*

1. Choose your preferred language (Java/Python/JS).
2. The bot will provide a code template.
3. Implement your logic using the greedy algorithm to find the minimum number of notes.
4. *(Java Specific)*: Implement the solution using only basic arrays (`int[]`), do not use `java.util.List` or other Collections Framework classes.
5. Submit the correct file (e.g., `Cash.java`).
