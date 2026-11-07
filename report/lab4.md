# Lab 4: Statements - NeemeScript

## Implementation Details

For this lab, NeemeScript was updated to support `print` statements and expression statements. The Parser was changed to return a list of statements instead of just parsing individual expressions. An `Evaluator` class was also added to execute these statements using the `StmtVisitor` interface.

Panic-mode error recovery was also added through the `synchronize()` method in the parser. This allows the parser to handle syntax errors without stopping the entire program. When an error occurs, it skips the invalid tokens until it reaches a point where it can continue parsing. This allows the interpreter to catch an error and move on to the remaining code instead of crashing.

## Setup and Run Instructions

Make sure Python 3 is installed before running the program. Open a terminal and navigate to the repository's root directory.

Run Test 1:
`python3 src/interpreter.py test/lab4/test1.ns`

Run Test 2:
`python3 src/interpreter.py test/lab4/test2.ns`

## Test Cases & Output

### Test Case 1: Panic-Mode Error Recovery

**Input:**
```text
"one"
true;
print 2 +
4 + 2;
```

**Output:**
```text
--- Scanned Tokens ---
STRING "one" one
TRUE true None
SEMICOLON ; None
PRINT print None
NUMBER 2 2.0
PLUS + None
NUMBER 4 4.0
PLUS + None
NUMBER 2 2.0
SEMICOLON ; None
EOF  None
[line 2] Error at 'true': Expect ';' after expression.
```

### Test Case 2: Print Statements

**Input:**
```text
print "one";
print true;
print 1 + 2;
print nil;
```

**Output:**
```text
--- Scanned Tokens ---
PRINT print None
STRING "one" one
SEMICOLON ; None
PRINT print None
TRUE true None
SEMICOLON ; None
PRINT print None
NUMBER 1 1.0
PLUS + None
NUMBER 2 2.0
SEMICOLON ; None
PRINT print None
NIL nil None
SEMICOLON ; None
EOF  None
one
true
3
nil
```
