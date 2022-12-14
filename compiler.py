# Amir Nejadmalayeri 98102487
# Mohammad javad Alaeddini 98170957
# Amir hossein bagheri jebelli 98109559
# Seyed hasan moafi 98171161

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

if len(tokens) != 0:
    line = tokens[0].line
    token_file.write(str(line) + '.\t')
    for t in tokens:
        if t.line != line:
            token_file.write('\n' + str(t.line) + '.\t')
            line = t.line
        token_file.write('(' + t.token_type + ', ' + t.lex + ') ')

token_file.write('\n')

error_file = open('lexical_errors.txt', 'w')

if len(sc.lexical_errors) != 0:
    line = sc.lexical_errors[0].line
    error_file.write(str(line) + '.\t')
    for e in sc.lexical_errors:
        if e.line != line:
            error_file.write('\n' + str(e.line) + '.\t')
            line = e.line
        error_file.write('(' + e.lex + ', ' + e.error_type + ') ')
else:
    error_file.write('There is no lexical error.')

symbol_table_file = open('symbol_table.txt', 'w')

line = 1
for s in sc.symbol_table:
    symbol_table_file.write(str(line) + '.\t' + s + '\n')
    line += 1
