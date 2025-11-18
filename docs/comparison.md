# Comparison: Arithmetic Mini-Language vs JSON/YAML
### Author: Alana Bernardez Banegas

Although my project is Option A2 (arithmetic language), it is still useful to compare my syntax to well-known data description languages like JSON and YAML.

---

## 📌 Purpose & Use-Cases

| Feature | My Language | JSON | YAML |
|--------|-------------|------|------|
| Purpose | Evaluate arithmetic expressions | Structured data | Structured data (human-friendly) |
| Focus | Computation | Serialization | Configuration |
| Supports Computation? | Yes | No | No |

---

## 📌 Syntax Differences

### My Language:
3 + 4 * (2 - 1)


### JSON:


{ "value": 3 }


### YAML:


value: 3


---

## 📌 Data Types

| Type | My Language | JSON | YAML |
|------|-------------|------|------|
| Number | Yes | Yes | Yes |
| Boolean | No | Yes | Yes |
| String | No | Yes | Yes |
| Objects | No | Yes | Yes |
| Arrays | No | Yes | Yes |

---

## 📌 Expression Capability

| Capability | My Language | JSON | YAML |
|-----------|-------------|------|------|
| Operators | + - * / % ^ | No | No |
| Parentheses | Yes | No | No |
| Precedence | Yes | No | No |
| Evaluation Engine | Yes | No | No |

---

## 📌 Summary
While JSON and YAML are data representation formats, my arithmetic language is a computational expression language. They serve entirely different problems, demonstrating the distinction between configuration languages and evaluative languages.
