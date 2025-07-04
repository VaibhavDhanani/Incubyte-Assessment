# Incubyte Assessment – String Calculator

This repository contains the implementation of the **String Calculator** as part of the **Incubyte Assessment**, following the principles of **Test-Driven Development (TDD)**.

## 🚀 What is TDD?

**Test-Driven Development (TDD)** is a software development approach where tests are written **before** the actual implementation. It follows the cycle of:

- **Red**: Write a failing test.
- **Green**: Write the minimal code to pass the test.
- **Refactor**: Improve the code while keeping all tests green.

This process ensures that code is reliable, testable, and maintainable from the start.

---

##  Problem Statement

Implement a method (in any language) `add(numbers: str) -> int` in Python (or equivalently, `public int add(String numbers)` in Java), that takes a string containing numbers separated by delimiters and returns their sum.

---

##  Features & Rules Implemented

- Empty string returns `0`
- Numbers are separated by commas `,` and/or newlines `\n`
- Custom delimiters can be defined:
  - Single-character delimiter: `"//;\n1;2"` → `3`
  - Delimiters of any length: `"//[***]\n1***2***3"` → `6`
  - Multiple delimiters: `"//[;^;][==]\n1;^;2==3"` → `6`
- Negative numbers raise an exception with a clear message:
  - 1. `"3,-4"` → Exception: `negatives not allowed`
  - 2. `//;\n\n1;-2;3\n\n\n-4\n-5` → Exception: `negatives not allowed : [-2, -4, -5]` 
- Numbers greater than `1000` are ignored:
  - Example: `"1001,2"` → `2`

---

## 📂 Method Signature

```python
def add(self, numbers: str) -> int
```

## Regarding Commits

Frequent commits can sometimes be seen as bad practice when they clutter the commit history, making it harder to analyze integrated work. However, since this project follows the **TDD** approach, I intentionally committed frequently to reflect the TDD cycle — writing a failing test, implementing code to pass the test, and then refactoring if possible. Each rule was implemented through this cycle, and corresponding commits were made at each stage to clearly demonstrate the TDD workflow.

## Test Result:
- A total of 13 test functions have been written, each containing an average of 3 test cases.
- ![image](https://github.com/user-attachments/assets/9b90102a-7013-464d-9271-d0cb3f5cc692)




