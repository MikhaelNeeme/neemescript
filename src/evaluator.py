from src.expr import ExprVisitor, Expr
from src.stmt import StmtVisitor, Stmt
from src.token import TokenType

class Evaluator(ExprVisitor, StmtVisitor):
    def interpret(self, statements: list[Stmt]):
        try:
            for statement in statements:
                if statement is not None:
                    self.execute(statement)
        except Exception as e:
            print(f"Runtime Error: {e}")

    def execute(self, stmt: Stmt):
        stmt.accept(self)

    def visit_expression_stmt(self, stmt):
        self.evaluate(stmt.expression)

    def visit_print_stmt(self, stmt):
        value = self.evaluate(stmt.expression)
        if value is None:
            print("nil")
        elif isinstance(value, bool):
            print(str(value).lower())
        elif isinstance(value, float) and value.is_integer():
            print(int(value))
        else:
            print(value)

    def evaluate(self, expr: Expr):
        return expr.accept(self)

    def is_truthy(self, obj):
        if obj is None: return False
        if isinstance(obj, bool): return obj
        if isinstance(obj, (int, float)): return obj != 0
        return True

    def as_number(self, obj):
        if isinstance(obj, bool): return 1.0 if obj else 0.0
        if isinstance(obj, (int, float)): return float(obj)
        return 0.0

    def visit_literal_expr(self, expr):
        return expr.value

    def visit_grouping_expr(self, expr):
        return self.evaluate(expr.expression)

    def visit_unary_expr(self, expr):
        right = self.evaluate(expr.right)
        if expr.operator.type == TokenType.MINUS:
            return -self.as_number(right)
        elif expr.operator.type == TokenType.BANG:
            return not self.is_truthy(right)
        return None

    def visit_binary_expr(self, expr):
        left = self.evaluate(expr.left)
        right = self.evaluate(expr.right)
        op = expr.operator.type

        if op == TokenType.MINUS: return self.as_number(left) - self.as_number(right)
        elif op == TokenType.SLASH: return self.as_number(left) / self.as_number(right)
        elif op == TokenType.STAR: return self.as_number(left) * self.as_number(right)
        elif op == TokenType.PLUS: return self.as_number(left) + self.as_number(right)
        elif op == TokenType.MODULO: return self.as_number(left) % self.as_number(right)
        elif op == TokenType.GREATER: return self.as_number(left) > self.as_number(right)
        elif op == TokenType.GREATER_EQUAL: return self.as_number(left) >= self.as_number(right)
        elif op == TokenType.LESS: return self.as_number(left) < self.as_number(right)
        elif op == TokenType.LESS_EQUAL: return self.as_number(left) <= self.as_number(right)
        elif op == TokenType.BANG_EQUAL: return left != right
        elif op == TokenType.EQUAL_EQUAL: return left == right
        return None
