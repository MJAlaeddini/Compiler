class Scanner:
    def __init__(self, input_file_name: str):
        self.input_file = open(input_file_name, 'r')
        self.error_file = open('lexical_errors.txt', 'w')
        self.symbol_table_file = open('symbol_table.txt', 'w')

    def get_next_token(self):
        pass  # ToDo

    def save_error(self):
        pass  # ToDo

    def save_symbol(self):
        pass  # ToDo
