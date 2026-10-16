# Lab 3: Parser - NeemeScript

## Expression Grammar, Precedence, and Associativity
The expression grammar parses tokens based on the following precedence levels (lowest to highest) and associativity:
1. **Equality:** `==`, `!=` (Left associative)
2. **Comparison:** `<`, `<=`, `>`, `>=` (Left associative)
3. **Term:** `+`, `-` (Left associative)
4. **Factor:** `*`, `/`, `%` (Left associative)
5. **Unary:** `!`, `-` (Right associative)
6. **Primary:** `NUMBER`, `STRING`, `true`, `false`, `nil`, `( expression )`

*Grammar changes since Lab 2:* None. We continue to support Lox's base operators alongside our custom modulo (`%`) operator.

## Setup and Run Instructions
Ensure Python 3 is installed. Navigate to the repository root.
**Interactive Mode:** `python3 src/interpreter.py`
**Source File Mode:** `python3 src/interpreter.py test/lab3/test_parser.ns`

## Test Cases & Results

### Valid Expressions
* **Test 1 (Precedence):**
  * *Input:* `1 + 2 * 3`
  * *Expected:* `(+ 1 (* 2 3))`
  * *Actual:* `(+ 1 (* 2 3))` (Match)
* **Test 2 (Grouping):**
  * *Input:* `(1 + 2) * 3`
  * *Expected:* `(* (group (+ 1 2)) 3)`
  * *Actual:* `(* (group (+ 1 2)) 3)` (Match)

### Syntax Errors
* **Error 1 (Unmatched Parenthesis):**
  * *Input:* `(1 + 2`
  * *Expected Error:* Expect ')' after expression.
  * *Actual:* `[line 1] Error at end: Expect ')' after expression.`
  * *Cause:* The `primary` rule consumes the left parenthesis and parses the expression, but hits EOF before finding the required right parenthesis.
* **Error 2 (Missing Operand):**
  * *Input:* `1 + `
  * *Expected Error:* Expect expression.
  * *Actual:* `[line 1] Error at end: Expect expression.`
  * *Cause:* The `term` rule matches `+` but fails to find a valid `factor` or `primary` expression afterward.
* **Error 3 (Trailing Tokens):**
  * *Input:* `1 + 2 trailing`
  * *Expected Error:* Unexpected trailing characters.
  * *Actual:* `[line 1] Error at 'trailing': Unexpected trailing characters after expression.`
  * *Cause:* The parser successfully completed a valid expression `1 + 2`, but tokens remained in the stream before `EOF`.

## Concrete Syntax Tree Diagram
**Expression:** `1 + 2 * 3`

```text
      Binary (+)
     /          \
Literal (1)   Binary (*)
             /          \
       Literal (2)   Literal (3)

Explanation: Because multiplication (*) has higher precedence (Factor) than addition (+) (Term), the term parser rule evaluates the +, keeping 1 as its left operand and recursively descending to the factor rule to evaluate 2 * 3 as its right operand. The AST printer recursively formats this hierarchy as (+ 1 (* 2 3)).

Limitations
No known limitations. The parser gracefully recovers from syntax errors without throwing Python exceptions.
