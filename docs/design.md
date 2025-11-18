# Design Document – Arithmetic Expression Mini-Language
### Author: Alana Bernardez Banegas
### Languages & Paradigms – Fall 2025

---

## 📌 1. Overview
This design document explains the architecture, algorithms, and implementation decisions used to build the Arithmetic Expression Mini-Language. The interpreter pipeline includes:

1. **Lexer** (Tokenization)  
2. **Parser** (Recursive Descent)  
3. **AST Construction**  
4. **Evaluator**  
5. **Error Handling**  
6. **REPL + Testing**

---

## 📌 2. Architecture Diagram

Input String
|
v
+---------------+
| Lexer |
+---------------+
|
Tokens |
v
+---------------+
| Parser |
+---------------+
|
v
+---------------+
| AST |
+---------------+
|
v
+---------------+
| Evaluator |
+---------------+
|
v
Final Result

---
## 📌 3. Lexer Design

### Responsibilities
- Convert characters → tokens  
- Track positions for error messages  
- Identify numbers, operators, and parentheses  
- Ignore whitespace  

### Key Decisions
- Numbers stored as int OR float depending on decimal  
- Single-character operators mapped directly  
- Invalid characters raise `LexerError`  

---

## 📌 4. Parser Design (Recursive Descent)

The parser mirrors the BNF grammar:

expr → term (("+" | "-") term)*
term → power (("" | "/" | "%") power)
power → unary ("^" power)?
unary → ("+" | "-") unary | primary
primary → NUMBER | "(" expr ")"

markdown
Copy code

### Operator Precedence (from lowest to highest)
1. `+` `-`
2. `*` `/` `%`
3. `^` (right-associative)
4. Unary `+` / Unary `-`

### Why Recursive Descent?
- Fits the grammar structure naturally  
- Easier to debug  
- Does not need parser generators  
- Good educational demonstration  

---

## 📌 5. AST Structure

### Nodes
- `NumberExpr`  
- `UnaryExpr`  
- `BinaryExpr`  

### Example
Expression: `2 * (3 + 4)`

markdown
Copy code
    (*)
   /   \
 (2)   (+)
       / \
     (3) (4)
yaml
Copy code

---

## 📌 6. Evaluator

### Approach:
- Depth-first traversal  
- Evaluate child nodes recursively  
- Apply operator logic  
- Convert integers to float internally  

### Runtime Errors Handled:
- Division by zero  
- Modulo by zero  
- Unsupported operator  

---

## 📌 7. Error Handling

### Types:
- `LexerError`  
- `ParseError`  
- `EvaluatorError`  

Errors include:
- Position in input  
- Token/character causing the issue  
- Clear explanation  

---

## 📌 8. REPL (Interactive Shell)

Features:
- Accepts user input  
- Evaluates expression  
- Displays result or error message  
- Supports `quit`/`exit`  

---

## 📌 9. Testing Strategy

### Valid tests:
- Precedence  
- Associativity  
- Parentheses  
- Floating-point  
- Unary operators  
- Modulo  

### Invalid tests:
- Missing parentheses  
- Unknown tokens (`abc`)  
- Unsupported operators  
- Incomplete expressions  

---

## 📌 10. Limitations
- No variables  
- No functions  
- No multiline input  
- No comments  
- Only expressions (not statements)  

---

## 📌 11. Future Work
- Variables and symbol table  
- Functions (`sin`, `max`)  
- Comments  
- Multi-expression programs  
- AST visualization  

---

## 📌 12. Summary
This design demonstrates a full interpreter pipeline aligned with theoretical concepts from the course: grammars, lexing, parsing, recursion, OOP, AST evaluation, and error handling.
