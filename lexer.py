import re


keywords = ['int', 'print', 'if', 'else', 'while', 'def']

tokens = []

def lexer(code):

    global tokens
    tokens = []

    token_pattern = r'[A-Za-z_][A-Za-z0-9_]*|\d+|==|<=|>=|<|>|\+|-|\*|/|=|;|\(|\)|\{|\}'

    words = re.findall(token_pattern, code)

    for word in words:

        if word in keywords:
            tokens.append(("KEYWORD", word))

        elif word.isdigit():
            tokens.append(("NUMBER", word))

        elif re.match(r'[A-Za-z_][A-Za-z0-9_]*', word):
            tokens.append(("IDENTIFIER", word))

        else:
            tokens.append(("SYMBOL", word))

    return tokens