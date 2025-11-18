# src/parser.py

from dataclasses import dataclass
from typing import List
from lexer import Token, TokenType, Lexer, LexerError


# ========== ERRORS ==========

class ParseError(Exception):
    """Error raised when the parser finds invalid syntax."""
    pass


class EvaluatorError(Exception):
    """Error raised during evaluation (e.g., division by zero)."""
    pass


# ========== AST NODE DEFINITIONS ==========

@dataclass
class Expr:
    """Base class for all expression nodes."""
    pass


@dataclass
class NumberExpr(Expr):
    value: float


@dataclass
class UnaryExpr(Expr):
    operator: TokenType  # PLUS or MINUS
    operand: Expr


@dataclass
class BinaryExpr(Expr):
    left: Expr
    operator: TokenType  # PLUS, MINUS, STAR, SLASH, PERCENT, CARET
    right: Expr


# ========== PARSER (RECURSIVE DESCENT) ==========

class Parser:
    """
    Recursive-descent parser for the arithmetic grammar.

    Grammar (simplified):

    <expr>   ::= <term> { ("+" | "-") <term> }
    <term>   ::= <power> { ("*" | "/" | "%") <power> }
    <power>  ::= <unary> [ "^" <power> ]
    <unary>  ::= [ "+" | "-" ] <unary> | <primary>
    <primary>::= <number> | "(" <expr> ")"
    """

    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.current = 0

    def _peek(self) -> Token:
        return self.tokens[self.current]

    def _advance(self) -> Token:
        token = self._peek()
        if token.type != TokenType.EOF:
            self.current += 1
        return token

    def _match(self, *types: TokenType) -> bool:
        if self._peek().type in types:
            self._advance()
            return True
        return False

    def _consume(self, type_: TokenType, message: str) -> Token:
        """Consume token of given type or raise error with message."""
        if self._peek().type == type_:
            return self._advance()
        token = self._peek()
        raise ParseError(
            f"{message} at position {token.position}, found '{token.lexeme}'"
        )

    def parse(self) -> Expr:
        """Parse full input and return the AST root."""
        expr = self._parse_expr()
        # Ensure no extra tokens after valid expression
        if self._peek().type != TokenType.EOF:
            token = self._peek()
            raise ParseError(
                f"Unexpected token '{token.lexeme}' at position {token.position}, "
                "expected end of expression."
            )
        return expr

    # <expr> ::= <term> { ("+" | "-") <term> }
    def _parse_expr(self) -> Expr:
        expr = self._parse_term()
        while self._match(TokenType.PLUS, TokenType.MINUS):
            op = self.tokens[self.current - 1]
            right = self._parse_term()
            expr = BinaryExpr(expr, op.type, right)
        return expr

    # <term> ::= <power> { ("*" | "/" | "%") <power> }
    def _parse_term(self) -> Expr:
        expr = self._parse_power()
        while self._match(TokenType.STAR, TokenType.SLASH, TokenType.PERCENT):
            op = self.tokens[self.current - 1]
            right = self._parse_power()
            expr = BinaryExpr(expr, op.type, right)
        return expr

    # <power> ::= <unary> [ "^" <power> ]  (right-associative)
    def _parse_power(self) -> Expr:
        left = self._parse_unary()
        if self._match(TokenType.CARET):
            op = self.tokens[self.current - 1]
            right = self._parse_power()
            return BinaryExpr(left, op.type, right)
        return left

    # <unary> ::= [ "+" | "-" ] <unary> | <primary>
    def _parse_unary(self) -> Expr:
        if self._match(TokenType.PLUS, TokenType.MINUS):
            op = self.tokens[self.current - 1]
            operand = self._parse_unary()
            return UnaryExpr(op.type, operand)
        return self._parse_primary()

    # <primary> ::= <number> | "(" <expr> ")"
    def _parse_primary(self) -> Expr:
        token = self._peek()
        if token.type == TokenType.NUMBER:
            self._advance()
            # store as float for mixed-mode arithmetic
            return NumberExpr(float(token.value))

        if token.type == TokenType.LPAREN:
            self._advance()
            expr = self._parse_expr()
            self._consume(TokenType.RPAREN, "Expected ')' after expression")
            return expr

        raise ParseError(
            f"Expected number or '(' at position {token.position}, "
            f"found '{token.lexeme}'"
        )


# ========== EVALUATOR ==========

class Evaluator:
    """
    Walks the AST and computes the numeric result.
    """

    def evaluate(self, expr: Expr) -> float:
        if isinstance(expr, NumberExpr):
            return expr.value
        if isinstance(expr, UnaryExpr):
            return self._eval_unary(expr)
        if isinstance(expr, BinaryExpr):
            return self._eval_binary(expr)
        raise EvaluatorError(f"Unknown expression type: {type(expr)}")

    def _eval_unary(self, expr: UnaryExpr) -> float:
        value = self.evaluate(expr.operand)
        if expr.operator == TokenType.PLUS:
            return +value
        elif expr.operator == TokenType.MINUS:
            return -value
        else:
            raise EvaluatorError(f"Unsupported unary operator: {expr.operator}")

    def _eval_binary(self, expr: BinaryExpr) -> float:
        left = self.evaluate(expr.left)
        right = self.evaluate(expr.right)

        if expr.operator == TokenType.PLUS:
            return left + right
        elif expr.operator == TokenType.MINUS:
            return left - right
        elif expr.operator == TokenType.STAR:
            return left * right
        elif expr.operator == TokenType.SLASH:
            if right == 0:
                raise EvaluatorError("Division by zero")
            return left / right
        elif expr.operator == TokenType.PERCENT:
            # Use integer modulo (rounded) for clarity
            li = int(round(left))
            ri = int(round(right))
            if ri == 0:
                raise EvaluatorError("Modulo by zero")
            return float(li % ri)
        elif expr.operator == TokenType.CARET:
            return left ** right
        else:
            raise EvaluatorError(f"Unsupported binary operator: {expr.operator}")
