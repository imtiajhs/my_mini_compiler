def parser(tokens, symbol_table):

    for i in range(len(tokens) - 1):

        if tokens[i][1] == 'int':

            var_name = tokens[i + 1][1]

            symbol_table.insert(var_name, "int")