# src/lexer.py

import re


def tokenize(code):
    tokens = []
    token_specification = [
        ('NUMBER', r'\d+'),
        ('ASSIGN', r'='),
        ('ID', r'[A-Za-z]+'),
        ('PRINT', r'print'),
        ('STRING', r'"[^"]*"'),
        ('PLUS', r'\+'),
        ('MINUS', r'-'),
        ('LPAREN', r'\('),
        ('RPAREN', r'\)'),
        ('SKIP', r'[ \t]+'),
        ('MISMATCH', r'.'),
    ]

    line_num = 1
    line_start = 0
    for mo in re.finditer('|'.join(f'(?P<{pair[0]}>{pair[1]})' for pair in token_specification), code):
        kind = mo.lastgroup
        value = mo.group()
        if kind == 'SKIP':
            continue
        elif kind == 'MISMATCH':
            raise RuntimeError(f'Unexpected character {value!r} at line {line_num}')
        tokens.append((kind, value))
    return tokens
