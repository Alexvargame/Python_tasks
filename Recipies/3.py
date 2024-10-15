import collections
import re


# Определение токенов
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
MINUS = r'(?P<MINUS>-)'
TIMES = r'(?P<TIMES>\*)'
DIVIDE = r'(?P<DIVIDE>/)'
LPAREN = r'(?P<LPAREN>\()'
RPAREN = r'(?P<RPAREN>\))'
WS = r'(?P<WS>\s+)'

master_pat = re.compile('|'.join([NUM, PLUS, MINUS, TIMES,
                                  DIVIDE, LPAREN, RPAREN, WS]))
# Токенизатор
Token = collections.namedtuple('Token', ['type','value'])

def generate_tokens(text):
    scanner = master_pat.scanner(text)
    for m in iter(scanner.match, None):
        tok = Token(m.lastgroup, m.group())
        if tok.type != 'WS':
            yield tok


class ExpressionEvaluator:

    def parse(self,text):
        self.tokens = generate_tokens(text)
     # Последний потребленный символ
        self.tok = None
     # Следующий токенизированный символ
        self.nexttok = None
     # Загрузить первый токен предварительного просмотра
        self._advance()
        return self.expr()
    
    def _advance(self):
     #Продвинуться на один токен вперед'
        self.tok, self.nexttok = self.nexttok, next(self.tokens, None)
        
    def _accept(self,toktype):
     #Проверить и потребить следующий токен, если он совпадает с toktype'
        if self.nexttok and self.nexttok.type == toktype:
            self._advance()
            return True
        else:
            return False
        
    def _expect(self,toktype):
    #Потребить следующий токен, если он совпадает с toktype, или возбудить SyntaxError'
        if not self._accept(toktype):
            raise SyntaxError('Expected ' + toktype)
     # Далее следуют правила грамматики

    def expr(self):
        "expression ::= term { ('+'|'-') term }*"
        print(self)
        exprval = self.term()
        print(exprval)
        while self._accept('PLUS') or self._accept('MINUS'):
            op = self.tok.type
            right = self.term()
            if op == 'PLUS':
                exprval += right
            elif op == 'MINUS':
                exprval -= right
        return exprval

    def term(self):
        "term ::= factor { ('*'|'/') factor }*"
        termval = self.factor()
        print(termval)
        while self._accept('TIMES') or self._accept('DIVIDE'):
            op = self.tok.type
            right = self.factor()
            if op == 'TIMES':
                termval *= right
            elif op == 'DIVIDE':
                termval /= right
        return termval
        
    def factor(self):
        "factor ::= NUM | ( expr )"
        if self._accept('NUM'):
            print(self.tok.value)
            return int(self.tok.value)
        elif self._accept('LPAREN'):
            exprval = self.expr()
            self._expect('RPAREN')
            return exprval
        else:
            raise SyntaxError('Expected NUMBER or LPAREN')

#Вот пример интерактивного использования класса
class ExpressionTreeBuilder(ExpressionEvaluator):
    def expr(self):
        "expression ::= term { ('+'|'-') term }"
        exprval = self.term()
        while self._accept('PLUS') or self._accept('MINUS'):
            op = self.tok.type
            right = self.term()
            if op == 'PLUS':
                exprval = ('+', exprval, right)
            elif op == 'MINUS':
                exprval = ('-', exprval, right)
        return exprval
    
    def term(self):
        "term ::= factor { ('*'|'/') factor }"
        termval = self.factor()
        while self._accept('TIMES') or self._accept('DIVIDE'):
            op = self.tok.type
            right = self.factor()
            if op == 'TIMES':
                termval = ('*', termval, right)
            elif op == 'DIVIDE':
                termval = ('/', termval, right)
        return termval
    
    def factor(self):
        'factor ::= NUM | ( expr )'
        if self._accept('NUM'):
            return int(self.tok.value)
        elif self._accept('LPAREN'):
            exprval = self.expr()
            self._expect('RPAREN')
            return exprval
        else:
            raise SyntaxError('Expected NUMBER or LPAREN')
 # Пример использования
if __name__ == '__main__':
    e = ExpressionEvaluator()
    print(e.parse('44'))
    e = ExpressionTreeBuilder()
    print(e.parse('2 + 3'),e.parse('2 + 3 * 4'),e.parse('2 + (3 + 4) * 5'),e.parse('2 + 3 + 4'))
