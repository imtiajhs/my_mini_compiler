def generate_assembly():

    assembly = []

    assembly.append(["1", "MOV a, 5"])
    assembly.append(["2", "MOV b, 10"])
    assembly.append(["3", "ADD a, b"])
    assembly.append(["4", "MOV c, a"])
    assembly.append(["5", "PRINT c"])

    return assembly