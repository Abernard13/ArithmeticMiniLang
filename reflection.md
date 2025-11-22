# Reflection – Arithmetic Expression Mini-Language  
### Author: Alana Bernardez Banegas  
### Languages & Paradigms – Fall 2025  
### Instructor: Dr. Omar  
### Project Category: A2 – BNF Grammar for Mini-Language

---

## 📌 Introduction
For this project, I implemented a complete arithmetic expression mini-language to demonstrate my understanding of fundamental language and paradigm concepts from the “Languages & Paradigms” course. The assignment required designing a formal BNF grammar, creating a tokenizer, implementing a recursive-descent parser, constructing an AST (Abstract Syntax Tree), and building an evaluator that executes expressions.

This reflection explains how I approached designing the language, why I made certain architectural choices, the paradigms this project demonstrates, challenges I encountered, and what I learned through building a small interpreter from scratch.

---

## 📌 Language Definition Using BNF
The first step of this project was designing a formal grammar to define what constitutes a valid arithmetic expression. My BNF grammar supports:

- Integers and floating-point numbers  
- Parentheses  
- Unary operators (+ and -)  
- Binary operators: +, -, *, /, %, ^  
- Correct operator precedence  
- Right-associative exponentiation  

The grammar serves as the “contract” of the language—an exact specification of its syntax. It is completely independent of Python code and represents the structure of the language in a theoretical and implementation-neutral form. This reflects core course concepts regarding formal languages, context-free grammars, and parsing theory.

---

## 📌 Lexer Design (Tokenization Phase)
After defining the grammar, I built a lexer that scans raw characters from the input string and produces a list of tokens. Each token contains:

- A type (e.g., NUMBER, PLUS, CARET)  
- The original lexeme  
- A numerical value (for numbers)  
- The character position (for error reporting)  

Design decisions:

- Support both integers and floats using digit scanning with optional decimal point  
- Ignore whitespace entirely  
- Raise `LexerError` for unsupported characters  
- Include the expression position in error messages  

The lexer is the first step of interpretation and demonstrates principles of lexical analysis used in languages such as Python, Java, C++, and JavaScript.

---

## 📌 Parser Design – Recursive Descent
To translate the token list into an AST, I implemented a recursive-descent parser. Each grammar rule is mapped to a Python function:

- `_parse_expr()` handles + and −  
- `_parse_term()` handles *, /, %  
- `_parse_power()` handles the right-associative ^ operator  
- `_parse_unary()` handles unary + and -  
- `_parse_primary()` handles numbers and parentheses  

Recursive descent was chosen because it directly matches the grammar structure, is easier to debug than table-driven parsers, and provides full control over associativity and precedence. This aligns with the course theme of understanding parsing strategies and compiler front-end design.

---

## 📌 Abstract Syntax Tree (AST)
The parser constructs an AST consisting of three node types:

- **NumberExpr** – stores numeric values  
- **UnaryExpr** – stores unary operators and their operand  
- **BinaryExpr** – stores binary operators and their left/right sub-expressions  

The AST represents the hierarchical structure of expressions. For example, `(1 + 2) * 3` becomes a tree where multiplication is the root, with addition and the constant 3 as children.

Implementing AST nodes as Python classes demonstrates object-oriented design concepts, including encapsulation and dynamic dispatch.

---

## 📌 Evaluation Phase (Interpreter)
The evaluator walks the AST recursively:

- Evaluate child nodes  
- Apply operators  
- Return numeric results  

Key behaviors:

- Mixed-mode arithmetic (ints and floats)  
- Division-by-zero and modulo-by-zero checks  
- Right-associative exponentiation (`2^3^2 = 2^(3^2)`)  
- Floating-point promotion for consistency  

This evaluation phase models the interpreter pattern used in scripting languages and demonstrates how expressions are executed after parsing.

---

## 📌 Error Handling (Lexing, Parsing, Evaluation)
I implemented three custom error types:

- **LexerError** – invalid characters  
- **ParseError** – incomplete or malformed syntax  
- **EvaluatorError** – runtime errors such as division by zero  

Each error includes:

- A clear message  
- The position in the input  
- The token or operator causing the issue  

This results in meaningful and user-friendly diagnostics, which is crucial for language tooling.

---

## 📌 Testing Strategy
The test suite includes:

### ✔️ Valid Expressions
- Operator precedence  
- Nested parentheses  
- Exponentiation chaining  
- Mixed integer/float expressions  
- Unary operators  
- Modulo behavior  

### ✔️ Invalid Expressions  
- Missing closing parentheses  
- Unexpected tokens  
- Unsupported operators (`//`)  
- Alphabetic characters (`abc`)  

Running tests before launching the REPL confirmed that all core features work correctly.

---

## 📌 Paradigms & Concepts Demonstrated

### 1. **Formal Language Theory**
BNF grammar illustrates syntax specifications used in compilers.

### 2. **Imperative Programming**
Lexer, parser, and evaluator use sequential control flow.

### 3. **Object-Oriented Programming**
AST node types are implemented with Python classes.

### 4. **Recursive Programming**
Both parsing and evaluation rely heavily on recursion.

### 5. **Interpreter Architecture**
The project follows the classic interpreter flow:

Source → Lexer → Parser → AST → Evaluator → Result

yaml
Copy code

### 6. **Error Handling Paradigms**
Distinguishing lexical, syntactic, and semantic errors mirrors real-world language design.

---

## 📌 Challenges & How I Solved Them

### **1. Operator Precedence**
I used separate grammar layers (`expr`, `term`, `power`, `unary`) to encode precedence naturally.

### **2. Right-Associative Exponentiation**
Exponentiation needed to evaluate as:
2^3^2 = 2^(3^2)

yaml
Copy code
I solved this using recursion inside `<power>` instead of a loop.

### **3. Meaningful Error Messages**
By tracking token positions, I ensured errors point to exactly where parsing failed.

### **4. Mixed-Mode Arithmetic**
Storing all numbers as floats simplified evaluation while preserving integer input support.

---

## 📌 What I Learned
By building this interpreter, I gained hands-on experience with:

- Grammar design  
- Lexical analysis  
- Recursive-descent parsing  
- AST construction  
- Expression evaluation  
- Error reporting  
- Interpreter architecture  

This project deepened my understanding of how languages like Python, C, and Java evaluate expressions and process source code internally.

---

## 📌 Future Enhancements
In future versions, I would like to add:

- Variables and assignments  
- A symbol table  
- Built-in functions (e.g., `sin`, `max`)  
- Multi-line program parsing  
- Control structures  
- Comments  
- AST visualization tools  

These additions would move the language toward a more complete mini-language.

---

## 📌 Conclusion
This project successfully demonstrates core concepts of programming language design. By defining a grammar, building a lexer, implementing a recursive-descent parser, constructing an AST, and evaluating expressions, I implemented an entire interpreter pipeline from scratch. This strengthened my understanding of parsing theory, compiler front-end design, recursion, and programming language paradigms.

