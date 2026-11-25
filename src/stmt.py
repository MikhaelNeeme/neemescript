from abc import ABC, abstractmethod
from src.expr import Expr

class StmtVisitor(ABC):
    @abstractmethod
    def visit_expression_stmt(self, stmt): pass
    @abstractmethod
    def visit_print_stmt(self, stmt): pass
    @abstractmethod
    def visit_var_stmt(self, stmt): pass
    @abstractmethod
    def visit_block_stmt(self, stmt): pass

class Stmt(ABC):
    @abstractmethod
    def accept(self, visitor: StmtVisitor): pass

class Expression(Stmt):
    def __init__(self, expression: Expr):
        self.expression = expression
    def accept(self, visitor: StmtVisitor):
        return visitor.visit_expression_stmt(self)

class Print(Stmt):
    def __init__(self, expression: Expr):
        self.expression = expression
    def accept(self, visitor: StmtVisitor):
        return visitor.visit_print_stmt(self)

# // --- start AI code
class Var(Stmt):
    def __init__(self, name, initializer: Expr):
        self.name = name
        self.initializer = initializer
    def accept(self, visitor: StmtVisitor):
        return visitor.visit_var_stmt(self)

class Block(Stmt):
    def __init__(self, statements: list[Stmt]):
        self.statements = statements
    def accept(self, visitor: StmtVisitor):
        return visitor.visit_block_stmt(self)
# // --- end AI code
