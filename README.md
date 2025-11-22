📘 Arithmetic Mini-Language

Category A2 – BNF Grammar for Mini-Language
Author: Alana Bernardez Banegas
Course: Languages & Paradigms – Fall 2025

📌 Overview

This project implements a mini arithmetic expression language built from scratch using:

A formal BNF grammar

A tokenizer (lexer)

A recursive-descent parser

An Abstract Syntax Tree (AST) evaluator

A REPL (Read–Eval–Print Loop)

A complete test suite for valid and invalid expressions

The interpreter supports integers, floats, parentheses, unary operators, and all required binary operators with correct precedence and associativity.

This project demonstrates key concepts from the course including formal grammars, lexical analysis, parsing techniques, AST construction, error handling, and interpreter design.

🧠 Language Features
Supported Operators

Addition: +

Subtraction: -

Multiplication: *

Division: /

Modulo: %

Exponentiation: ^ (right-associative)

Supported Syntax

Integers and floating-point numbers

Parentheses ( ... )

Unary operators: +x, -x

Mixed-mode arithmetic (ints + floats)

Error Handling

The interpreter raises clear errors for:

Invalid characters

Unexpected tokens

Missing parentheses

Unsupported operators (//, etc.)

Division or modulo by zero

📐 BNF Grammar
<expr>     ::= <term> { ("+" | "-") <term> }
<term>     ::= <power> { ("*" | "/" | "%") <power> }
<power>    ::= <unary> [ "^" <power> ]        ; right-associative
<unary>    ::= [ "+" | "-" ] <unary> | <primary>
<primary>  ::= <number> | "(" <expr> ")"

🗂 Project Structure
ArithmeticMiniLang/
├── README.md
├── reflection.pdf
├── docs/
│   └── grammar.txt
└── src/
    ├── lexer.py
    ├── parser.py
    └── main.py

▶️ Running the Program
1. Navigate to the project directory
cd ArithmeticMiniLang/src

2. Run the interpreter
python3 main.py


The program will automatically:

Run the complete test suite

Enter the interactive REPL

🧪 Example Usage (REPL)
>>> 1+2*3
= 7.0

>>> (1+2)*3
= 9.0

>>> 2^3^2
= 512.0

>>> -(-2)
= 2.0


Exit with:

>>> quit

✔️ Tests Included

The built-in test suite checks:

Operator precedence

Nested parentheses

Exponentiation associativity

Floats and integers

Unary operations

Invalid syntax and error messages

💡 General Design Notes

The lexer scans characters and produces tokens.

The parser implements a recursive-descent strategy that matches the BNF grammar exactly.

The AST evaluator executes expressions recursively.

All numeric values are stored as floats to support mixed arithmetic.

Error messages include character positions for clarity.

Full design discussion is included in reflection.pdf.

🙌 Acknowledgments

Created for the Languages & Paradigms course to demonstrate formal grammar design, parsing, recursion, and interpreter architecture.
