# Ripgrep bug report

## Description

When using dumping searching result as json format, the submatch "end" field is not correct. Here is a minimum example to repoduce the issue.

## Repoduce

Run the following command
```bash
# in this directory
python3 test.py
```

## Expected Output

```bash
# some other outputs ...
Match length: 3560
Submatch start/end: (294, 3579)
Submatch length: 3267
Submatch start + length: 3561
```
As you can see, submatch end (3579) is even greater than match length (3560). But submatch start + length is correct somehow.
