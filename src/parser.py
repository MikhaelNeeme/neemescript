from src.token import Token, TokenType
from src.expr import Binary, Grouping, Literal, Unary

class ParseError(Exception):
    pass

class Parser:
    def __init__(self, tokens: list[Token]):
        self.tokens = tokens
        self.current = 0
        self.has_error = False

    def parse(self):
        try:
            if self.is_at_end():
                return None

            expr = self.expression()

            # Lab requirement: Report unexpected trailing tokens instead of silently ignoring them
            if not self.is_at_end() and self.peek().type != TokenType.EOF:
                self.error(self.peek(), "Unexpected trailing characters after expression.")

            return expr
        except ParseError:
            return None

    # # --- start AI code
    def expression(self):
        return self.equality()

    def equality(self):
        expr = self.comparison()
        while self.match(TokenType.BANG_EQUAL, TokenType.EQUAL_EQUAL):
            operator = self.previous()
            right = self.comparison()
            expr = Binary(expr, operator, right)
        return expr

    def comparison(self):
        expr = self.term()
        while self.match(TokenType.GREATER, TokenType.GREATER_EQUAL, TokenType.LESS, TokenType.LESS_EQUAL):
            operator = self.previous()
            right = self.term()
            expr = Binary(expr, operator, right)
        return expr

    def term(self):
        expr = self.factor()
        while self.match(TokenType.MINUS, TokenType.PLUS):
            operator = self.previous()
            right = self.factor()
            expr = Binary(expr, operator, right)
        return expr

    def factor(self):
        expr = self.unary()
        while self.match(TokenType.SLASH, TokenType.STAR, TokenType.MODULO):
            operator = self.previous()
            right = self.unary()
            expr = Binary(expr, operator, right)
        return expr

    def unary(self):
        if self.match(TokenType.BANG, TokenType.MINUS):
            operator = self.previous()
            right = self.unary()
            return Unary(operator, right)
        return self.primary()

    def primary(self):
        if self.match(TokenType.FALSE): return Literal(False)
        if self.match(TokenType.TRUE): return Literal(True)
        if self.match(TokenType.NIL): return Literal(None)

        if self.match(TokenType.NUMBER, TokenType.STRING):
            return Literal(self.previous().literal)

        if self.match(TokenType.LEFT_PAREN):
            expr = self.expression()
            self.consume(TokenType.RIGHT_PAREN, "Expect ')' after expression.")
            return Grouping(expr)

        raise self.error(self.peek(), "Expect expression.")
    # # --- end AI code

    def match(self, *types) -> bool:
        for token_type in types:
            if self.check(token_type):
                self.advance()
                return True
        return False

    def consume(self, token_type, message: str):
        if self.check(token_type):
            return self.advance()
        raise self.error(self.peek(), message)

    def check(self, token_type) -> bool:
        if self.is_at_end():
            return False
        return self.peek().type == token_type

    def advance(self):
        if not self.is_at_end():
            self.current += 1
        return self.previous()

    def is_at_end(self) -> bool:
        return self.peek().type == TokenType.EOF

    def peek(self) -> Token:
        return self.tokens[self.current]

    def previous(self) -> Token:
        return self.tokens[self.current - 1]

    def error(self, token: Token, message: str):
        self.has_error = True
        if token.type == TokenType.EOF:
            print(f"[line {token.line}] Error at end: {message}")
        else:
            print(f"[line {token.line}] Error at '{token.lexeme}': {message}")
        return ParseError()

    def synchronize(self):
        self.advance()
        while not self.is_at_end():
            if self.previous().type == TokenType.SEMICOLON:
                return
            if self.peek().type in [TokenType.FUNC, TokenType.LET, TokenType.CONST, TokenType.IF, TokenType.WHILE, TokenType.PRINT, TokenType.RETURN]:
                return
            self.advance()
