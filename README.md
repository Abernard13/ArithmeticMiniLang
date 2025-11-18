# Arithmetic Expression Mini-Language  
### Languages & Paradigms – Final Project  
### Author: Alana Bernardez Banegas  
### Due: December 11, 2025

## 📌 Overview
This project implements a fully working **arithmetic expression language** with its own:

- **BNF grammar**
- **Lexer / Tokenizer**
- **Recursive-Descent Parser**
- **AST (Abstract Syntax Tree)**
- **Evaluator**
- **Error handling**
- **Test cases**
- **Interactive REPL**

The mini-language supports:

- Integers and floating-point numbers  
- Parentheses  
- Unary operators (`+`, `-`)  
- Binary operators:  
  `+`, `-`, `*`, `/`, `%`, `^`  
- Correct operator precedence and associativity  
- Right-associative exponentiation (e.g., `2^3^2 = 2^9 = 512`)  

---

## 📌 Repository Structure
ArithmeticMiniLang/
├── README.md
├── reflection.md
├── docs/
│ └── grammar.md
└── src/
├── lexer.py
├── parser.py
└── main.py
