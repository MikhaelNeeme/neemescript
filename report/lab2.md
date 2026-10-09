# Lab 2: AST Printer - NeemeScript


## Design Choices and Differences from Lox

- I used the same four main expression types as Lox: Binary, Grouping, Literal, and Unary.
- I  added the modulo (`%`) operator in Lab 1, so we included it in the AST printer to support the additional operator in NeemeScript.
- When printing expressions, Python's `None` is converted to `"nil"` to match NeemeScript's syntax.

## Setup and Run Instructions

Make sure Python 3 is installed and open a terminal in the root folder of the repository. Run the following command to test the AST printer:

```bash
python3 test/lab2/test_printer.py
```

The script prints the hardcoded expressions so their output can be checked against the expected results.

## Test Cases and Results

### Test Case 1: Math and Grouping

- **Purpose:** Check that binary expressions, unary expressions, grouping, and number literals print correctly.
- **Hard-coded AST:** `-(123) * (45.67)`
- **Expected Output:** `(* (- 123) (group 45.67))`
- **Actual Output:** `(* (- 123) (group 45.67))`

The output matches the expected result.

### Test Case 2: Booleans and Equality

- **Purpose:** Check that boolean literals and logical operators print correctly.
- **Hard-coded AST:** `true == !false`
- **Expected Output:** `(== True (! False))`
- **Actual Output:** `(== True (! False))`

The output matches the expected result.

### Test Case 3: Modulo, Nil, and Nested Grouping

- **Purpose:** Check the modulo (`%`) operator, the conversion of `nil`, and nested expressions.
- **Hard-coded AST:** `(10 % 3) != nil`
- **Expected Output:** `(!= (group (% 10 3)) nil)`
- **Actual Output:** `(!= (group (% 10 3)) nil)`

The output matches the expected result.

## Limitations

All current test cases pass, i dont think there arre any issues with the AST printer at this time.# Lab 2: AST Printer - NeemeScript

## Expression Grammar
The expression grammar for NeemeScript, based on formal notation, is defined:
```text
expression → literal | unary | binary | grouping ;
literal    → NUMBER | STRING | "true" | "false" | "nil" ;
grouping   → "(" expression ")" ;
unary      → ( "-" | "!" ) expression ;
binary     → expression operator expression ;
operator   → "==" | "!=" | "<" | "<=" | ">" | ">=" | "+" | "-" | "*" | "/" | "%" ;
