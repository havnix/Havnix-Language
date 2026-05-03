import re
import math
import random


class HavnixExpressionError(Exception):
    pass


def tokenize(expr, variables):
    tokens = []
    i = 0
    while i < len(expr):
        c = expr[i]

        if c in ' \t':
            i += 1
            continue

        if c == '!' and i + 1 < len(expr) and expr[i + 1] == '=':
            tokens.append(('CMP', '!='))
            i += 2
            continue
        if c == '=' and i + 1 < len(expr) and expr[i + 1] == '=':
            tokens.append(('CMP', '=='))
            i += 2
            continue
        if c == '>' and i + 1 < len(expr) and expr[i + 1] == '=':
            tokens.append(('CMP', '>='))
            i += 2
            continue
        if c == '<' and i + 1 < len(expr) and expr[i + 1] == '=':
            tokens.append(('CMP', '<='))
            i += 2
            continue
        if c == '>':
            tokens.append(('CMP', '>'))
            i += 1
            continue
        if c == '<':
            tokens.append(('CMP', '<'))
            i += 1
            continue

        if c in '+-*/%':
            tokens.append(('OP', c))
            i += 1
            continue

        if c == '(':
            tokens.append(('LPAREN', '('))
            i += 1
            continue
        if c == ')':
            tokens.append(('RPAREN', ')'))
            i += 1
            continue
        if c == '[':
            tokens.append(('LBRACKET', '['))
            i += 1
            continue
        if c == ']':
            tokens.append(('RBRACKET', ']'))
            i += 1
            continue
        if c == ',':
            tokens.append(('COMMA', ','))
            i += 1
            continue
        if c == '.':
            tokens.append(('DOT', '.'))
            i += 1
            continue
        if c == '{':
            tokens.append(('LBRACE', '{'))
            i += 1
            continue
        if c == '}':
            tokens.append(('RBRACE', '}'))
            i += 1
            continue
        if c == ':':
            tokens.append(('COLON', ':'))
            i += 1
            continue

        if c == '"' or c == "'":
            quote = c
            i += 1
            s = ''
            while i < len(expr) and expr[i] != quote:
                if expr[i] == '\\' and i + 1 < len(expr):
                    next_c = expr[i + 1]
                    if next_c == 'n':
                        s += '\n'
                    elif next_c == 't':
                        s += '\t'
                    elif next_c == '\\':
                        s += '\\'
                    elif next_c == quote:
                        s += quote
                    else:
                        s += next_c
                    i += 2
                else:
                    s += expr[i]
                    i += 1
            if i < len(expr):
                i += 1
            tokens.append(('STRING', s))
            continue

        if c == '$':
            i += 1
            name = ''
            while i < len(expr) and (expr[i].isalnum() or expr[i] == '_' or ord(expr[i]) > 127):
                name += expr[i]
                i += 1
            tokens.append(('VAR', name))
            continue

        if c.isdigit():
            num = ''
            while i < len(expr) and (expr[i].isdigit() or expr[i] == '.'):
                num += expr[i]
                i += 1
            if '.' in num:
                tokens.append(('NUMBER', float(num)))
            else:
                tokens.append(('NUMBER', int(num)))
            continue

        word = ''
        while i < len(expr) and (expr[i].isalnum() or expr[i] == '_' or ord(expr[i]) > 127):
            word += expr[i]
            i += 1

        if word:
            if word == 'صاح':
                tokens.append(('BOOL', True))
            elif word == 'غلط':
                tokens.append(('BOOL', False))
            elif word == 'فاضي':
                tokens.append(('NULL', None))
            elif word == 'و':
                tokens.append(('AND', 'و'))
            elif word == 'أو' or word == 'او':
                tokens.append(('OR', 'أو'))
            elif word == 'مو':
                tokens.append(('NOT', 'مو'))
            else:
                tokens.append(('IDENT', word))
            continue

        raise HavnixExpressionError(f"رمز غير معروف: '{c}'")

    return tokens


class ExpressionParser:
    def __init__(self, tokens, variables, builtin_funcs=None, user_func_caller=None):
        self.tokens = tokens
        self.pos = 0
        self.variables = variables
        self.builtin_funcs = builtin_funcs or {}
        self._user_func_caller = user_func_caller

    def peek(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None

    def consume(self, expected_type=None):
        token = self.peek()
        if token is None:
            raise HavnixExpressionError("نهاية التعبير بشكل غير متوقع")
        if expected_type and token[0] != expected_type:
            raise HavnixExpressionError(f"متوقع {expected_type} لكن وجد {token[0]}")
        self.pos += 1
        return token

    def parse(self):
        result = self.parse_or()
        return result

    def parse_or(self):
        left = self.parse_and()
        while self.peek() and self.peek()[0] == 'OR':
            self.consume()
            right = self.parse_and()
            left = left or right
        return left

    def parse_and(self):
        left = self.parse_not()
        while self.peek() and self.peek()[0] == 'AND':
            self.consume()
            right = self.parse_not()
            left = left and right
        return left

    def parse_not(self):
        if self.peek() and self.peek()[0] == 'NOT':
            self.consume()
            value = self.parse_not()
            return not value
        return self.parse_comparison()

    def parse_comparison(self):
        left = self.parse_addition()
        if self.peek() and self.peek()[0] == 'CMP':
            op = self.consume()[1]
            right = self.parse_addition()
            if op == '==':
                return left == right
            elif op == '!=':
                return left != right
            elif op == '>':
                return left > right
            elif op == '<':
                return left < right
            elif op == '>=':
                return left >= right
            elif op == '<=':
                return left <= right
        return left

    def parse_addition(self):
        left = self.parse_multiplication()
        while self.peek() and self.peek()[0] == 'OP' and self.peek()[1] in '+-':
            op = self.consume()[1]
            right = self.parse_multiplication()
            if op == '+':
                if isinstance(left, str) or isinstance(right, str):
                    left = str(left) + str(right)
                else:
                    left = left + right
            elif op == '-':
                left = left - right
        return left

    def parse_multiplication(self):
        left = self.parse_unary()
        while self.peek() and self.peek()[0] == 'OP' and self.peek()[1] in '*/%':
            op = self.consume()[1]
            right = self.parse_unary()
            if op == '*':
                left = left * right
            elif op == '/':
                if right == 0:
                    raise HavnixExpressionError("لا يمكن القسمة على صفر")
                left = left / right
            elif op == '%':
                left = left % right
        return left

    def parse_unary(self):
        if self.peek() and self.peek()[0] == 'OP' and self.peek()[1] == '-':
            self.consume()
            return -self.parse_primary()
        return self.parse_primary()

    def parse_primary(self):
        token = self.peek()
        if token is None:
            raise HavnixExpressionError("تعبير غير مكتمل")

        if token[0] == 'NUMBER':
            self.consume()
            return token[1]

        if token[0] == 'STRING':
            self.consume()
            return self._interpolate_string(token[1])

        if token[0] == 'BOOL':
            self.consume()
            return token[1]

        if token[0] == 'NULL':
            self.consume()
            return None

        if token[0] == 'VAR':
            self.consume()
            var_name = token[1]
            value = self.variables.get(var_name)
            if value is None and var_name not in self.variables:
                raise HavnixExpressionError(f"المتغير '${var_name}' غير موجود")
            while self.peek() and self.peek()[0] == 'LBRACKET':
                self.consume()
                index = self.parse()
                self.consume('RBRACKET')
                if isinstance(value, list):
                    value = value[int(index)]
                elif isinstance(value, dict):
                    value = value[index]
                else:
                    raise HavnixExpressionError(f"المتغير '${var_name}' لا يدعم الفهرسة")
            return value

        if token[0] == 'IDENT':
            self.consume()
            name = token[1]
            if self.peek() and self.peek()[0] == 'LPAREN':
                self.consume()
                args = []
                if self.peek() and self.peek()[0] != 'RPAREN':
                    args.append(self.parse())
                    while self.peek() and self.peek()[0] == 'COMMA':
                        self.consume()
                        args.append(self.parse())
                self.consume('RPAREN')
                if name in self.builtin_funcs:
                    return self.builtin_funcs[name](*args)
                if self._user_func_caller:
                    return self._user_func_caller(name, args)
                raise HavnixExpressionError(f"الدالة '{name}' غير موجودة")
            if name in self.variables:
                value = self.variables[name]
                while self.peek() and self.peek()[0] == 'LBRACKET':
                    self.consume()
                    index = self.parse()
                    self.consume('RBRACKET')
                    if isinstance(value, list):
                        value = value[int(index)]
                    elif isinstance(value, dict):
                        value = value[index]
                return value
            raise HavnixExpressionError(f"معرف غير معروف: '{name}'")

        if token[0] == 'LPAREN':
            self.consume()
            value = self.parse()
            self.consume('RPAREN')
            return value

        if token[0] == 'LBRACKET':
            self.consume()
            items = []
            if self.peek() and self.peek()[0] != 'RBRACKET':
                items.append(self.parse())
                while self.peek() and self.peek()[0] == 'COMMA':
                    self.consume()
                    items.append(self.parse())
            self.consume('RBRACKET')
            return items

        if token[0] == 'LBRACE':
            self.consume()
            d = {}
            if self.peek() and self.peek()[0] != 'RBRACE':
                key = self.parse()
                self.consume('COLON')
                val = self.parse()
                d[key] = val
                while self.peek() and self.peek()[0] == 'COMMA':
                    self.consume()
                    key = self.parse()
                    self.consume('COLON')
                    val = self.parse()
                    d[key] = val
            self.consume('RBRACE')
            return d

        raise HavnixExpressionError(f"تعبير غير متوقع: {token}")

    def _interpolate_string(self, text):
        def replace_var(match):
            var_name = match.group(1)
            idx = match.group(2)
            val = self.variables.get(var_name, f"${var_name}")
            if idx is not None:
                try:
                    if isinstance(val, (list, dict)):
                        key = int(idx) if idx.isdigit() else idx
                        val = val[key]
                except (IndexError, KeyError):
                    pass
            return str(val)
        text = re.sub(r'\$(\w+)\[(\w+)\]', replace_var, text)
        text = re.sub(r'\$(\w+)', lambda m: str(self.variables.get(m.group(1), '$' + m.group(1))), text)
        return text


def evaluate_expression(expr, variables, builtin_funcs=None, user_func_caller=None):
    expr = expr.strip()
    if not expr:
        return None
    try:
        tokens = tokenize(expr, variables)
        if not tokens:
            return None
        parser = ExpressionParser(tokens, variables, builtin_funcs, user_func_caller)
        return parser.parse()
    except HavnixExpressionError:
        raise
    except Exception as e:
        raise HavnixExpressionError(f"خطأ في تقييم التعبير: {e}")
