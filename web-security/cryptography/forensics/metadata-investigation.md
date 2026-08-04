
---

### 3. Digital Forensics — File Metadata Investigation

```markdown
# File Metadata Forensics Lab

## Platform

Local forensic exercise

## Category

Digital Forensics

## Objective

The goal of this exercise was to investigate a sample file and determine
what useful information could be recovered without executing it.

## Environment

The sample was created specifically for this lab and analyzed locally.

## Initial Analysis

I started by identifying the file type and calculating its cryptographic
hash.

Example commands:

```bash
file sample.jpg
sha256sum sample.jpg
