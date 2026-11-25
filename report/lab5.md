# Lab 5: Variables and Scope - NeemeScript

## Implementation Details & Design Choices

For this lab, I added support for variables in NeemeScript. This includes declaring variables with `let`, accessing their values, changing their values, and using block scope with `{ ... }`. To handle this, I used an `Environment` class that keeps track of variables and connects each scope to its surrounding environment.

### Design Choices

* **Using a variable before declaring it:** If a variable is accessed or assigned a value before it has been declared, the interpreter reports a runtime error (`Runtime Error: Undefined variable '<name>'.`).

* **Declaring a variable without a value:** Variables can be declared without giving them an initial value. For example, `let c;` is allowed, and the variable is automatically given the value `nil`.

* **Declaring a variable more than once:** Declaring the same variable more than once in the same scope is allowed. The new declaration replaces the previous value in that environment. For example, `let a = 1; let a = "redeclared";` changes the value of `a` to `"redeclared"`. However, declaring a variable with the same name inside an inner block does not change the variable in the outer block. Instead, the inner variable has its own value.

## Setup and Run Instructions

Make sure Python 3 is installed and open a terminal in the repository's root directory (`~/neemescript-lab1`).

The following commands can be used to run each test:

* **Variables Test:** `python3 src/interpreter.py test/lab5/test_vars.ns`
* **Block Scope Test:** `python3 src/interpreter.py test/lab5/test_scope.ns`
* **Syntax Errors Test:** `python3 src/interpreter.py test/lab5/test_errors.ns`
* **Runtime Error Test:** `python3 src/interpreter.py test/lab5/test_runtime_error.ns`

---

## Test Cases & Output

### 1. Variable Declaration, Access, Assignment, and Design Choices

**Input (`test/lab5/test_vars.ns`):**

```text
let a = 1;
let b = 2;
print a + b;
a = 10;
print a;
let c;
print c;
let a = "redeclared";
print a;
```

**Output:**

```text
3
10
nil
redeclared
```

This test checks that variables can be declared, used in expressions, and assigned new values. It also checks what happens when a variable is declared without an initial value and when the same variable is declared again. As shown in the output, the interpreter correctly calculates `a + b`, updates the value of `a`, and assigns `nil` to `c` because no value was provided.

### 2. Block Scope (Textbook Example)

**Input (`test/lab5/test_scope.ns`):**

```javascript
let a = "global a";
let b = "global b";
let c = "global c";
{
  let a = "outer a";
  let b = "outer b";
  {
    let a = "inner a";
    print a;
    print b;
    print c;
  }
  print a;
  print b;
  print c;
}
print a;
print b;
print c;
```

**Output:**

```text
inner a
outer b
global c
outer a
outer b
global c
global a
global b
global c
```

**Explanation of Output:**

Every time the interpreter enters a new `{ ... }` block, it creates a new `Environment` connected to the environment around it. This allows variables to have different values depending on which block they are being used in.

1. **Inside the innermost block:** The variable `a` uses the value `"inner a"` because it was declared in that block. The variable `b` was not declared there, so the interpreter looks in the outer block and finds `"outer b"`. The same thing happens with `c`, but since it is not declared in either block, the interpreter finds `"global c"`.

2. **After leaving the innermost block:** The interpreter returns to the outer block. At this point, the inner block's variables are no longer accessible. The values of `a` and `b` are `"outer a"` and `"outer b"`, while `c` still uses its global value of `"global c"`.

3. **After leaving the outer block:** The interpreter returns to the global environment. The variables now have their original values: `"global a"`, `"global b"`, and `"global c"`.

This test shows that block scope is working correctly. Variables declared inside a block stay within that block, and they do not overwrite variables with the same names in outer environments.

### 3. Error Handling

**Syntax Errors Input (`test/lab5/test_errors.ns`):**

```javascript
let a = 1;
a + 1 = 2;
{
  let b = 2;
```

**Output:**

```text
[line 2] Error at '=': Invalid assignment target.
[line 5] Error at end: Expect '}' after block.
```

There are two errors in this test:

* **Invalid assignment target:** On line 2, `a + 1` is an expression, not a variable name. Since the interpreter only allows values to be assigned to variables, the parser reports an invalid assignment target.

* **Missing closing brace:** On line 3, a block is opened with `{`, but there is no closing `}`. When the parser reaches the end of the file on line 5, it reports that the closing brace is missing.

**Runtime Error Input (`test/lab5/test_runtime_error.ns`):**

```text
print x;
```

**Output:**

```text
Runtime Error: Undefined variable 'x'.
```

This test checks what happens when the program tries to access a variable that has never been declared. Since `x` does not exist in the current environment or any enclosing environment, the interpreter reports an undefined variable error instead of trying to print a value.
