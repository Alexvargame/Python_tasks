import types

class Node:
    pass
class UnaryOperator(Node):
    def __init__(self, operand):
        self.operand = operand
class BinaryOperator(Node):
    def __init__(self, left, right):
        self.left = left
        self.right = right
class Add(BinaryOperator):
    pass
class Sub(BinaryOperator):
    pass
class Mul(BinaryOperator):
    pass
class Div(BinaryOperator):
    pass
class Negate(UnaryOperator):
    pass
class Number(Node):
    def __init__(self, value):
        self.value = value

t1 = Sub(Number(3), Number(4))
t2 = Mul(Number(2), t1)
t3 = Div(t2, Number(5))
t4 = Add(Number(1), t3)
print(t1)
class NodeVisitor:
    def visit(self, node):
        stack=[node]
        last_result=None
        while stack:
            try:
                last=stack[-1]
                if isinstance(last,types.GeneratorType):
                    stack.append(last.send(last_result))
                    last_resulr=None
                elif isinstance(last,Node):
                    stack.append(self._visit(stack.pop()))
                else:
                    last_result=stack.pop()
            except StopIteration:
                stack.pop()
        return last_result

    def _visit(self,node):
        methname = 'visit_' + type(node).__name__
        meth = getattr(self, methname, None)
        if meth is None:
            meth = self.generic_visit
        return meth(node)
    def generic_visit(self, node):
        raise RuntimeError('No {} method'.format('visit_' + type(node).__name__))

class Evaluator(NodeVisitor):
    def visit_Number(self, node):
        return node.value
    def visit_Add(self, node):
        yield (yield node.left) +(yield node.right)
    def visit_Sub(self, node):
        yield (yield node.left) - (yield node.right)
    def visit_Mul(self, node):
        yield (yield node.left) * (yield node.right)
    def visit_Div(self, node):
        yield (yield node.left) / ( yield node.right)
    def visit_Negate(self, node):
        yield -(yield node.operand)
a=Number(1)
for n in range(1,6):
    a=Mul(a,Number(n))
    
e=Evaluator()
e.visit(a)
print(e.visit(a))


class StackCode(NodeVisitor):
    def generate_code(self, node):
        self.instructions = []
        self.visit(node)
        return self.instructions
    def visit_Number(self, node):
        self.instructions.append(('PUSH', node.value))
    def binop(self, node, instruction):
        self.visit(node.left)
        self.visit(node.right)
        self.instructions.append((instruction,))
    def visit_Add(self, node):
        self.binop(node, 'ADD')
    def visit_Sub(self, node):
        self.binop(node, 'SUB')
    def visit_Mul(self, node):
        self.binop(node, 'MUL')
    def visit_Div(self, node):
        self.binop(node, 'DIV')
    def unaryop(self, node, instruction):
        self.visit(node.operand)
        self.instructions.append((instruction,))
    def visit_Negate(self, node):
        self.unaryop(node, 'NEG')

s=StackCode()
s.generate_code(t4)
print(s.generate_code(t4))
