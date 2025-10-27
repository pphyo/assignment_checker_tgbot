*Number to Myanmar Counting Words*

Write a function that converts a given non-negative integer into its Myanmar textual representation, followed by "ကျပ်".

The conversion should follow standard Myanmar counting units (e.g., ဆယ်, ရာ, ထောင်, သောင်း, သိန်း, သန်း, ကုဋေ).

**Simplified Grammar Rules:**

➤ For numbers like 1000, 10000, 100000 etc., both "တ" (Ta) and "တစ်" (Tit) prefixes are acceptable (e.g., "တထောင်ကျပ်" or "တစ်ထောင်ကျပ်" are both considered correct by the checker). Your solution can choose one consistent style.
➤ Do *not* use complex grammatical suffix changes like "ထောင့်" or "ရာ့". Always use the base unit name followed by the next number/unit.
➤ Example: 1101 should be `"တထောင့်တစ်ရာ့တစ်ကျပ်"` **NOT** `"တထောင့်တစ်ရာတစ်ကျပ်"` (This rule is simplified for the assignment). **Use `"တထောင်တစ်ရာတစ်ကျပ်"`**.

*Examples:*

➤ Input: `1000` ➔ Output: `"တထောင်ကျပ်"` (or `"တစ်ထောင်ကျပ်"`)
➤ Input: `10101` ➔ Output: `"တသောင်းတရာတကျပ်"` (or `"တစ်သောင်းတစ်ရာတစ်ကျပ်"`)
➤ Input: `110101` ➔ Output: `"တသိန်းတသောင်းတရာတကျပ်"` (or `"တစ်သိန်းတစ်သောင်းတစ်ရာတစ်ကျပ်"`)
➤ Input: `1234` ➔ Output: `"တထောင်နှစ်ရာသုံးဆယ့်လေးကျပ်"` (or `"တစ်ထောင်..."`)
➤ Input: `111` ➔ Output: `"တစ်ရာတစ်ဆယ့်တစ်ကျပ်"`
➤ Input: `0` ➔ Output: `"သုညကျပ်"`

---

*Instructions:*

1. Choose your preferred language (Java/Python/JS).

2. The bot will provide a code template.

3. Implement your logic following the simplified grammar rules and submit the correct file (e.g., `NumberToMyanmarWord.java`).
