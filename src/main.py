# src/main.py

from lexer import Lexer, LexerError
from parser import Parser, ParseError, Evaluator, EvaluatorError


def evaluate_expression(expr_str: str) -> float:
    """
    Helper function: given an expression string,
    run lexer -> parser -> evaluator and return result.
    """
    lexer = Lexer(expr_str)
    tokens = lexer.tokenize()

    parser = Parser(tokens)
    ast = parser.parse()

    evaluator = Evaluator()
    return evaluator.evaluate(ast)


def run_repl():
    """
    Simple interactive loop to test the language.
    """
    print("Mini Arithmetic Language REPL")
    print("Type an expression, or 'quit' to exit.\n")
    while True:
        try:
            line = input(">>> ")
        except EOFError:
            break

        if line.strip().lower() in {"quit", "exit"}:
            break

        if not line.strip():
            continue

        try:
            result = evaluate_expression(line)
            print("= ", result)
        except (LexerError, ParseError, EvaluatorError) as e:
            print("Error:", e)


def run_tests():
    """
    Basic test suite: some valid and invalid expressions.
    """
    print("Running tests...\n")

    test_cases = [
        ("1+2*3", 7.0),
        ("(1+2)*3", 9.0),
        ("2^3^2", 512.0),           # 2^(3^2) = 2^9 = 512
        ("-3 + 5", 2.0),
        ("3 + 4 * 2 / (1 - 5)^2", 3.5),
        ("7 % 3", 1.0),
        ("7 % 4 + 2", 5.0),
        ("3.5 + 2", 5.5),
        ("-(-2)", 2.0),
    ]

    for expr, expected in test_cases:
        try:
            result = evaluate_expression(expr)
            passed = abs(result - expected) < 1e-9
            status = "PASS" if passed else "FAIL"
            print(f"{status}: {expr} = {result}, expected {expected}")
        except Exception as e:
            print(f"ERROR: {expr} -> {e}")

    # Invalid syntax tests (should raise errors)
    invalid = [
        "1 +",
        "* 3",
        "3 + (4 *",
        "3 // 2",   # unsupported operator
        "abc",      # invalid characters
    ]

    print("\nInvalid tests (expect errors):")
    for expr in invalid:
        try:
            _ = evaluate_expression(expr)
            print(f"FAIL (no error): {expr}")
        except (LexerError, ParseError, EvaluatorError) as e:
            print(f"OK (error as expected): {expr} -> {e}")


if __name__ == "__main__":
    # First run tests, then start REPL
    run_tests()
    print("\n--- Entering REPL ---\n")
    run_repl()
