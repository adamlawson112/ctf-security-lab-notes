
---

### 4. Reverse Engineering — Simple Local Crackme

这个可以自己写一个很小的 C 程序再分析，不需要碰任何真实软件。

```markdown
# Basic Reverse Engineering Lab

## Platform

Local intentionally created binary

## Category

Reverse Engineering

## Environment

I compiled a small program specifically for this exercise and analyzed the
resulting binary on my own system.

## Objective

The goal was to understand how a simple validation routine appears after a
program is compiled.

## Test Program

The test application asks the user for a value and compares it against a
hard-coded value.

The program was created solely for this exercise.

## Static Analysis

I loaded the compiled binary into:

- Ghidra
- strings

I first searched for readable strings and then inspected references to the
input validation function.

## Analysis

Ghidra's decompiler helped identify the section responsible for comparing
user input.

I observed:

`[DESCRIBE THE FUNCTION OR COMPARISON YOU ACTUALLY SAW]`

## Dynamic Testing

I executed the binary locally using several different inputs and compared
the resulting program behavior.

## Result

The analysis allowed me to understand how the original validation logic was
represented in the compiled binary.

## Tools Used

- GCC
- Ghidra
- strings
- Linux command-line utilities

## Lessons Learned

This exercise helped me practice:

- Identifying strings inside binaries
- Navigating functions in Ghidra
- Understanding basic control flow
- Comparing source code with compiled output

The binary was created by me specifically for this lab.
