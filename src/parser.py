# src/parser.py

from lexer import tokenize


def parse(tokens):
    # Пример простого парсера для выражений и присваиваний
    idx = 0

    def parse_assignment():
        nonlocal idx
        if tokens[idx][0] == 'ID' and tokens[idx + 1][0] == 'ASSIGN':
            var_name = tokens[idx][1]
            idx += 2
            expr = parse_expression()
            return ('ASSIGNMENT', var_name, expr)
        return None

    def parse_expression():
        nonlocal idx
        if tokens[idx][0] == 'NUMBER':
            value = int(tokens[idx][1])
            idx += 1
            return ('NUMBER', value)
        elif tokens[idx][0] == 'ID':
            var_name = tokens[idx][1]
            idx += 1
            return ('VARIABLE', var_name)
        raise SyntaxError("Unexpected token: " + str(tokens[idx]))

    stmt = parse_assignment() or parse_expression()
    return stmt
