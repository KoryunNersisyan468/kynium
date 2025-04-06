# src/main.py

from lexer import tokenize
from parser import parse
from interpreter import Interpreter

def run_code(code):
    tokens = tokenize(code)  # Токенизация исходного кода
    ast = parse(tokens)       # Парсинг токенов в абстрактное синтаксическое дерево
    interpreter = Interpreter()
    interpreter.interpret(ast)  # Выполнение кода

if __name__ == "__main__":
    import sys
    with open(sys.argv[1], 'r') as file:
        run_code(file.read())
