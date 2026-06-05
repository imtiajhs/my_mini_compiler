from advanced_error_checker import check_advanced_syntax
from lexer import lexer
from parser import parser
from symbol_table import SymbolTable
from intermediate_code import generate_TAC
from assembly_generator import generate_assembly

# =========================
# READ SOURCE CODE
# =========================

with open("input.txt", "r") as file:
    code = file.read()

# =========================
# ERROR CHECKING (MUST FIRST)
# =========================

errors = check_advanced_syntax(code)

if errors:
    print("\n========== ERRORS FOUND ==========\n")
    for e in errors:
        print(e)
    exit()

# =========================
# LEXICAL ANALYSIS
# =========================

tokens = lexer(code)

print("\nTOKENS:\n")

for token in tokens:
    print(token)

with open("tokens.txt", "w") as file:
    for token in tokens:
        file.write(str(token) + "\n")

# =========================
# SYMBOL TABLE
# =========================

symbol_table = SymbolTable()

parser(tokens, symbol_table)

symbols = symbol_table.display()

print("\nSYMBOL TABLE (HASH):\n")

for row in symbols:
    print("Index:", row[0], " Name:", row[1], " Type:", row[2])

with open("symbol_table.txt", "w") as file:
    file.write("INDEX\tNAME\tTYPE\n")
    for row in symbols:
        file.write(f"{row[0]}\t{row[1]}\t{row[2]}\n")

# =========================
# TAC (INTERMEDIATE CODE)
# =========================

tac = generate_TAC()

print("\nTHREE ADDRESS CODE:\n")

for line in tac:
    print(line[0], "   ", line[1])

with open("tac.txt", "w") as file:
    for line in tac:
        file.write(line[0] + "    " + line[1] + "\n")

# =========================
# ASSEMBLY CODE
# =========================

assembly = generate_assembly()

print("\nASSEMBLY CODE:\n")

for line in assembly:
    print(line[0], "   ", line[1])

with open("assembly.txt", "w") as file:
    for line in assembly:
        file.write(line[0] + "    " + line[1] + "\n")