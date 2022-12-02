import string

class Scanner:

    def __init__(self, input_file_name: str):
        self.symbols = [';', '=', '/', '+', '*', '-', '<', '>', ':', '[', ']', '{', '}', '(', ')']
        self.whiteSpace = ['\n', ' ', '\r', '\t', '\v', '\f']
        self.Keywords = ['if', 'else', 'void', 'int', 'while', 'break', 'switch', 'case', 'default', 'return', 'endif']
        self.line = 1
        self.alphabet = list(string.ascii_lowercase) + list(string.ascii_uppercase)
        self.lexical_errors = []

        self.input_file = open(input_file_name, 'r')
        self.token_file = open('tokens.txt', 'w')
        self.error_file = open('lexical_errors.txt', 'w')
        self.symbol_table_file = open('symbol_table.txt', 'w')

    def get_next_token(self):

        next_char = self.input_file.read(1)
        if '0' <= next_char <= '9':
            lex = next_char
            while True:
                next_char = self.input_file.read(1)
                if '0' <= next_char <= '9':
                    lex = lex + next_char
                elif next_char in self.symbols or next_char in self.whiteSpace:
                    self.input_file.seek(self.input_file.tell() - 1)
                    return Token('NUM', self.line, lex)
                elif next_char in self.alphabet:
                    lex += next_char
                    self.lexical_errors.append(Error("Invalid number", self.line, lex))
                else:
                    lex += next_char
                    self.lexical_errors.append(Error("Invalid input", self.line, lex))
        elif next_char == '\n':
            self.line += 1

        pass  # ToDo

    def save_error(self):
        pass  # ToDo

    def save_symbol(self):
        pass  # ToDo


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
