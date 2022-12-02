import scanner

sc = scanner.Scanner('input.txt')
tokens = []

while True:
    token = sc.get_next_token()

    if token is not None:
        if token == 'exit':
            break

        tokens.append(token)

token_file = open('tokens.txt', 'w')

line = tokens[0].line
token_file.write(str(line) + '.\t')
for t in tokens:
    if t.line != line:
        token_file.write('\n' + str(line) + '.\t')
        line = t.line
    token_file.write('(' + t.token_type + ', ' + t.lex + ') ')

error_file = open('lexical_errors.txt', 'w')

line = sc.lexical_errors[0].line
error_file.write(str(line) + '.\t')
for e in sc.lexical_errors:
    if e.line != line:
        error_file.write('\n' + str(line) + '.\t')
    error_file.write('(' + e.lex + ', ' + e.error_type + ') ')

symbol_table_file = open('symbol_table.txt', 'w')

line = 1
for s in sc.symbol_table:
    symbol_table_file.write(str(line) + '\t' + s + '\n')
    line += 1
