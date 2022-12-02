import string


class Scanner:

    def __init__(self, input_file_name: str):
        self.symbols = [';', '=', '/', '+', '*', '-', '<', ':', '[', ']', '{', '}', '(', ')', ',']
        self.whiteSpace = ['\n', ' ', '\r', '\t', '\v', '\f']
        self.line_break = ['\n', '\r', '\v', '\f']
        self.keywords = ['if', 'else', 'void', 'int', 'while', 'break', 'switch', 'case', 'default', 'return', 'endif']
        self.digit = list(string.digits)
        self.line = 1
        self.alphabet = list(string.ascii_lowercase) + list(string.ascii_uppercase)
        self.lexical_errors = []
        self.symbol_table = ['if', 'else', 'void', 'int', 'while', 'break', 'switch', 'case', 'default', 'return', 'endif']

        self.input_file = open(input_file_name, 'r')

    def get_next_token(self):

        next_char = self.input_file.read(1)
        if next_char in self.digit:
            lex = next_char
            while True:
                t = self.input_file.tell()
                next_char = self.input_file.read(1)
                if next_char in self.digit:
                    lex = lex + next_char
                elif next_char in self.symbols or next_char in self.whiteSpace:
                    self.input_file.seek(t)
                    return Token('NUM', self.line, lex)
                elif next_char in self.alphabet:
                    lex += next_char
                    self.lexical_errors.append(Error("Invalid number", self.line, lex))
                    return None
                else:
                    lex += next_char
                    self.lexical_errors.append(Error("Invalid input", self.line, lex))
                    return None
        elif next_char in self.alphabet:
            lex = next_char
            while True:
                t = self.input_file.tell()
                next_char = self.input_file.read(1)
                if next_char in self.alphabet or next_char in self.digit:
                    lex = lex + next_char
                elif next_char in self.symbols or next_char in self.whiteSpace:
                    self.input_file.seek(t)
                    if lex not in self.symbol_table:
                        self.symbol_table.append(lex)
                    if lex in self.keywords:
                        return Token('KEYWORD', self.line, lex)
                    else:
                        return Token('ID', self.line, lex)
                else:
                    lex += next_char
                    self.lexical_errors.append(Error("Invalid input", self.line, lex))
                    return None
        elif next_char in self.symbols:
            lex = next_char
            if next_char == '/':
                next_char = self.input_file.read(1)
                lex += next_char
                if next_char == '*':
                    while True:
                        next_char = self.input_file.read(1)
                        lex += next_char
                        if next_char == '*':
                            if self.input_file.read(1) == '/':
                                return
                            else:
                                self.input_file.seek(self.input_file.tell() - 1)
                        elif next_char == '':
                            self.lexical_errors.append(Error("Unclosed comment", self.line, lex[:7] + '...'))
                            return
                elif next_char == '/':
                    while True:
                        next_char = self.input_file.read(1)
                        if next_char in self.line_break or next_char == '':
                            self.line += 1
                            return
                elif next_char in self.symbols or next_char in self.whiteSpace or next_char in self.digit or next_char in self.alphabet:
                    self.input_file.seek(self.input_file.tell() - 1)
                    return Token('SYMBOL', self.line, '/')
                else:
                    self.lexical_errors.append(Error("Invalid input", self.line, '/' + next_char))
            elif next_char == '=':
                next_char = self.input_file.read(1)
                if next_char == '=':
                    return Token('SYMBOL', self.line, '==')
                elif next_char in self.symbols or next_char in self.whiteSpace or next_char in self.digit or next_char in self.alphabet:
                    self.input_file.seek(self.input_file.tell() - 1)
                    return Token('SYMBOL', self.line, '=')
                else:
                    self.lexical_errors.append(Error("Invalid input", self.line, '=' + next_char))
            elif next_char == '*':
                next_char = self.input_file.read(1)
                if next_char == '/':
                    self.lexical_errors.append(Error("Unmatched comment", self.line, '*/'))
                elif next_char in self.symbols or next_char in self.whiteSpace or next_char in self.digit or next_char in self.alphabet:
                    self.input_file.seek(self.input_file.tell() - 1)
                    return Token('SYMBOL', self.line, '*')
                else:
                    self.lexical_errors.append(Error("Invalid input", self.line, '*' + next_char))
            else:
                return Token('SYMBOL', self.line, next_char)
        elif next_char in self.whiteSpace:
            if next_char in self.line_break:
                self.line += 1
        elif next_char == '':
            return 'exit'
        else:
            self.lexical_errors.append(Error("Invalid input", self.line, next_char))


class Token:
    def __init__(self, token_type: str, line: int, lex: str):
        self.token_type = token_type
        self.line = line
        self.lex = lex


class Error:
    def __init__(self, error_type: str, line: int, lex: str):
        self.error_type = error_type
        self.line = line
        self.lex = lex


class Symbol:
    def __init__(self, lex: str):
        self.lex = lex
