def write_file(filename, lines):
    with open(filename, "w") as f:
        f.writelines(lines)
