import re

def check_advanced_syntax(code):

    errors = []
    declared_vars = set()

    lines = code.split("\n")

    open_braces = 0

    for i, line in enumerate(lines):

        line_num = i + 1
        line = line.strip()

        if line == "":
            continue

        # =========================
        # BRACES CHECK
        # =========================

        if "{" in line:
            open_braces += 1

        if "}" in line:
            open_braces -= 1

        if open_braces < 0:
            errors.append(f"Line {line_num}: Extra closing brace '}}'")

        # =========================
        # VARIABLE DECLARATION
        # =========================

        if line.startswith("int "):

            parts = line.replace(";", "").split()

            if len(parts) >= 2:
                declared_vars.add(parts[1])

        # =========================
        # ASSIGNMENT CHECK
        # =========================

        if "=" in line and not line.startswith("int"):

            var = line.split("=")[0].strip()

            if var not in declared_vars and not var in ["print"]:

                errors.append(f"Line {line_num}: Undefined variable '{var}'")

        # =========================
        # INVALID EXPRESSION CHECK
        # =========================

        if "=" in line and "+" in line:

            expr = line.split("=")[1].replace(";", "").strip()

            if re.search(r'[+\-*/]{2,}', expr):
                errors.append(f"Line {line_num}: Invalid expression '{expr}'")

        # =========================
        # PRINT CHECK
        # =========================

        if "print" in line:

            if "(" not in line or ")" not in line:
                errors.append(f"Line {line_num}: Invalid print syntax")

    # =========================
    # FINAL BRACE CHECK
    # =========================

    if open_braces != 0:
        errors.append("Error: Missing closing brace '}'")