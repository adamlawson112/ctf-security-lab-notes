# XOR Encoding Analysis

## Platform

Local CTF-style exercise

## Category

Cryptography

## Environment

I created and analyzed the challenge locally for educational purposes.

## Objective

The goal was to understand how repeating-key XOR transforms plaintext and
how known information about the message can help during analysis.

## Challenge Data

The exercise consisted of a hexadecimal encoded ciphertext:

`[YOUR TEST CIPHERTEXT]`

## Initial Analysis

I first converted the hexadecimal representation into raw bytes using Python.

I then examined:

- Ciphertext length
- Repeated byte patterns
- Candidate key lengths
- Expected plaintext structure

## Approach

I wrote a small Python script to apply XOR operations to the ciphertext.

Example structure:

```python
def xor_bytes(data, key):
    return bytes(
        value ^ key[i % len(key)]
        for i, value in enumerate(data)
    )
