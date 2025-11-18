# src/lexer.py

from dataclasses import dataclass
from enum import Enum, auto
from typing import Optional, Union, List


class TokenType(Enum):
    NUMBER = auto()
    PLUS = auto()
    MINUS = auto()
    STAR = auto()
    SLASH = auto()
    PERCENT = auto()
    CARET = auto()
    LPAREN = auto()
    RPAREN = auto()
    EOF = auto()


@dataclass
class Token:
    type: TokenType
    lexeme: str
    value: Optional[Union[int, float]]
    position: int   # index in the original string


class LexerError(Exception):
    """Error raised when the lexer encounters an invalid character."""
    pass


class Lexer:
    def __init__(self, text: str):
        self.text = text
        self.length = len(text)
        self.pos = 0

    def _peek(self) -> Optional[str]:
        """Return current character without consuming it."""
        if self.pos >= self.length:
            return None
        return self.text[self.pos]

    def _advance(self) -> Optional[str]:
        """Consume and return current character."""
        ch = self._peek()
        if ch is not None:
            self.pos += 1
        return ch

    def _skip_whitespace(self):
        """Skip spaces, tabs, newlines."""
        while self._peek() is not None and self._peek().isspace():
            self._advance()

    def _number(self, start_pos: int) -> Token:
        """
        Read a number: digits [ "." digits ]
        Supports integers (e.g., 123) and floats (e.g., 3.14).
        """
        num_str = ""
        dot_seen = False

        while True:
            ch = self._peek()
            if ch is not None and ch.isdigit():
                num_str += ch
                self._advance()
            elif ch == "." and not dot_seen:
                dot_seen = True
                num_str += ch
                self._advance()
            else:
                break

        if dot_seen:
            value: Union[int, float] = float(num_str)
        else:
            value = int(num_str)

        return Token(TokenType.NUMBER, num_str, value, start_pos)

    def next_token(self) -> Token:
        """
        Return the next token from the input.
        """
        self._skip_whitespace()

        start_pos = self.pos
        ch = self._peek()

        if ch is None:
            return Token(TokenType.EOF, "", None, self.pos)

        # Numbers
        if ch.isdigit():
            return self._number(start_pos)

        # Single-character tokens
        self._advance()
        if ch == "+":
            return Token(TokenType.PLUS, ch, None, start_pos)
        if ch == "-":
            return Token(TokenType.MINUS, ch, None, start_pos)
        if ch == "*":
            return Token(TokenType.STAR, ch, None, start_pos)
        if ch == "/":
            return Token(TokenType.SLASH, ch, None, start_pos)
        if ch == "%":
            return Token(TokenType.PERCENT, ch, None, start_pos)
        if ch == "^":
            return Token(TokenType.CARET, ch, None, start_pos)
        if ch == "(":
            return Token(TokenType.LPAREN, ch, None, start_pos)
        if ch == ")":
            return Token(TokenType.RPAREN, ch, None, start_pos)

        # Unknown character
        raise LexerError(f"Unexpected character '{ch}' at position {start_pos}")

    def tokenize(self) -> List[Token]:
        """Tokenize the whole input into a list of tokens."""
        tokens: List[Token] = []
        while True:
            token = self.next_token()
            tokens.append(token)
            if token.type == TokenType.EOF:
                break
        return tokens
