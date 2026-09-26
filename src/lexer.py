from dataclasses import dataclass


@dataclass
class Token:
    type: str
    value: str
    line: int
    column: int


KEYWORDS = {
    "if42": "IF",
    "else42": "ELSE",
    "while42": "WHILE",
    "return42": "RETURN",
    "int42": "INT",
    "float42": "FLOAT",
    "bool42": "BOOL",
    "struct42": "STRUCT",
    "func42": "FUNC",
    "true42": "TRUE",
    "false42": "FALSE",
}


class Lexer:
    def __init__(self, source):
        self.source = source
        self.pos = 0
        self.line = 1
        self.column = 1
        self.tokens = []

    def advance(self):
        ch = self.source[self.pos]
        self.pos += 1

        if ch == "\n":
            self.line += 1
            self.column = 1
        else:
            self.column += 1

        return ch

    def tokenize(self):
        while self.pos < len(self.source):
            ch = self.source[self.pos]

            if ch.isspace():
                self.advance()
                continue

            if ch.isalpha() or ch == "_":
                self.scan_identifier()
                continue

            if ch.isdigit():
                self.scan_number()
                continue

            if ch == "+":
                self.tokens.append(
                    Token("PLUS", "+", self.line, self.column)
                )
                self.advance()
                continue

            if ch == "-":
                self.tokens.append(
                    Token("MINUS", "-", self.line, self.column)
                )
                self.advance()
                continue

            # আরও operators/symbols এখানে থাকবে

            raise SyntaxError(
                f"Unexpected character '{ch}' "
                f"at line {self.line}, column {self.column}"
            )

        self.tokens.append(
            Token("EOF", "", self.line, self.column)
        )

        return self.tokens

    def scan_identifier(self):
        start_line = self.line
        start_column = self.column
        value = ""

        while self.pos < len(self.source):
            ch = self.source[self.pos]

            if ch.isalnum() or ch == "_":
                value += self.advance()
            else:
                break

        token_type = KEYWORDS.get(value, "IDENTIFIER")

        self.tokens.append(
            Token(
                token_type,
                value,
                start_line,
                start_column
            )
        )

    def scan_number(self):
        start_line = self.line
        start_column = self.column
        value = ""

        while self.pos < len(self.source):
            ch = self.source[self.pos]

            if ch.isdigit():
                value += self.advance()
            else:
                break

        self.tokens.append(
            Token(
                "NUMBER",
                value,
                start_line,
                start_column
            )
        )
