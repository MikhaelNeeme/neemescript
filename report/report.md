# Lab 1: Scanning Report - NeemeScript

## Language Overview

The name of my programming language is **NeemeScript**. It is based on Lox, but I made a few changes to the syntax and added a few features to make it different from the original language.

One of the main changes is that NeemeScript uses `func` instead of `fun` when declaring a function. I also added `let` and `const` for variable declarations. `let` can be used for regular variables, while `const` is meant for values that should not be changed. I also added the modulo `%` operator. This allows the language to find the remainder when one number is divided by another.

## Lexical Grammar

The scanner reads the source code and breaks it into different tokens. NeemeScript uses regular expressions to describe some of the basic parts of the language, such as identifiers, numbers, and strings.

### Identifiers

Identifiers are used for names such as variables and functions. An identifier has to start with a letter or an underscore. After the first character, it can contain letters, numbers, or underscores.

The regular expression for identifiers is:

```text
[a-zA-Z_][a-zA-Z0-9_]*
```

For example, these are valid identifiers:

```text
name
student1
_myVariable
test_value
```

An identifier cannot start with a number. For example, `1name` would not be valid.

### Number Literals

NeemeScript supports both whole numbers and decimal numbers. A number starts with at least one digit. If a decimal number is being used, it can have a decimal point followed by more digits.

The regular expression for number literals is:

```text
[0-9]+(\.[0-9]+)?
```

Some examples of valid numbers are:

```text
10
25
3.14
100.5
```

The decimal part is optional, which means whole numbers are also valid.

### String Literals

String literals are written using double quotation marks. The scanner starts at the first quotation mark and continues reading until it finds the closing quotation mark.

The regular expression for string literals is:

```text
"[^"\n]*"
```

Some examples of valid strings are:

```text
"Hello"
"NeemeScript is working"
"Hello World!"
```

A string cannot contain a quotation mark that would be interpreted as the closing quotation mark. Strings also cannot continue onto another line with this format.

## Setup and Running the Program

Python 3 needs to be installed before running NeemeScript. After getting the repository, open a terminal and navigate to the root folder of the project.

To run a NeemeScript source file, use:

```bash
python3 src/interpreter.py test/lab1/test_script.ns
```

The `src/interpreter.py` file runs the interpreter, and `test/lab1/test_script.ns` is the NeemeScript file that is being tested.

When this command is run, the interpreter reads the source file and processes the code. This allows the scanner and the rest of the interpreter to be tested using an actual NeemeScript program.

## Summary

NeemeScript is a modified version of Lox with a few changes to its syntax and features. It uses `func` instead of `fun`, adds `let` and `const` for variable declarations, and includes the `%` modulo operator. The scanner recognizes identifiers, numbers, and strings using regular expressions. The language can be tested by running the interpreter with Python and providing a `.ns` source file.
