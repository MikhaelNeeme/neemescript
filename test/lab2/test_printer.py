import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from src.token import Token, TokenType
from src.expr import Binary, Grouping, Literal, Unary
from src.ast_printer import AstPrinter

def run_tests():
    printer = AstPrinter()
    print("--- Lab 2 AST Printer Tests ---")

    # Test 1: -(123) * (45.67)
    test1 = Binary(
        Unary(Token(TokenType.MINUS, "-", None, 1), Literal(123)),
        Token(TokenType.STAR, "*", None, 1),
        Grouping(Literal(45.67))
    )
    print("Test 1 (Math & Grouping):")
    print("Expected: (* (- 123) (group 45.67))")
    print(f"Actual:   {printer.print(test1)}\n")

    # Test 2: true == !false
    test2 = Binary(
        Literal(True),
        Token(TokenType.EQUAL_EQUAL, "==", None, 1),
        Unary(Token(TokenType.BANG, "!", None, 1), Literal(False))
    )
    print("Test 2 (Booleans & Equality):")
    print("Expected: (== True (! False))")
    print(f"Actual:   {printer.print(test2)}\n")

    # Test 3: (10 % 3) != nil
    test3 = Binary(
        Grouping(
            Binary(Literal(10), Token(TokenType.MODULO, "%", None, 1), Literal(3))
        ),
        Token(TokenType.BANG_EQUAL, "!=", None, 1),
        Literal(None)
    )
    print("Test 3 (Modulo, Nil & Nested Grouping):")
    print("Expected: (!= (group (% 10 3)) nil)")
    print(f"Actual:   {printer.print(test3)}\n")

if __name__ == "__main__":
    run_tests()
